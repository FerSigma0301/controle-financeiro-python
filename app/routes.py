from datetime import date
from decimal import Decimal, InvalidOperation
import csv
import io

from flask import Blueprint, jsonify, make_response, redirect, render_template, request, url_for
from sqlalchemy import and_, func

from app.models import Transaction, db

bp = Blueprint("finance", __name__)


def parse_form():
    try:
        amount = Decimal(request.form["amount"].replace(",", "."))
    except (KeyError, InvalidOperation):
        raise ValueError("Informe um valor válido.") from None
    due_date = date.fromisoformat(request.form["due_date"])
    transaction_type = request.form["transaction_type"]
    status = request.form.get("status", "pending")
    if transaction_type not in {"income", "expense"}:
        raise ValueError("Tipo de lançamento inválido.")
    if status not in {"paid", "pending"}:
        raise ValueError("Status inválido.")
    if amount <= 0:
        raise ValueError("O valor deve ser maior que zero.")
    return Transaction(
        description=request.form["description"].strip(),
        amount=amount,
        transaction_type=transaction_type,
        category=request.form["category"].strip(),
        due_date=due_date,
        status=status,
    )


def filtered_transactions():
    query = Transaction.query
    start = request.args.get("start")
    end = request.args.get("end")
    if start:
        query = query.filter(Transaction.due_date >= date.fromisoformat(start))
    if end:
        query = query.filter(Transaction.due_date <= date.fromisoformat(end))
    if request.args.get("type") in {"income", "expense"}:
        query = query.filter_by(transaction_type=request.args["type"])
    if request.args.get("category"):
        query = query.filter_by(category=request.args["category"])
    if request.args.get("status") in {"paid", "pending"}:
        query = query.filter_by(status=request.args["status"])
    return query.order_by(Transaction.due_date.desc(), Transaction.id.desc())


@bp.get("/")
def dashboard():
    transactions = filtered_transactions().all()
    incomes = sum((t.amount for t in transactions if t.transaction_type == "income"), Decimal("0"))
    expenses = sum((t.amount for t in transactions if t.transaction_type == "expense"), Decimal("0"))
    categories = [row[0] for row in db.session.query(Transaction.category).distinct().order_by(Transaction.category).all()]
    return render_template("dashboard.html", transactions=transactions, incomes=incomes, expenses=expenses, balance=incomes - expenses, categories=categories)


@bp.post("/transactions")
def create_transaction():
    try:
        transaction = parse_form()
    except (ValueError, KeyError) as error:
        return render_template("dashboard.html", error=str(error), transactions=[], incomes=0, expenses=0, balance=0, categories=[]), 400
    db.session.add(transaction)
    db.session.commit()
    return redirect(url_for("finance.dashboard"))


@bp.post("/transactions/<int:transaction_id>/delete")
def delete_transaction(transaction_id):
    transaction = db.get_or_404(Transaction, transaction_id)
    db.session.delete(transaction)
    db.session.commit()
    return redirect(url_for("finance.dashboard"))


@bp.get("/api/summary")
def summary():
    rows = filtered_transactions().all()
    return jsonify({"incomes": float(sum((t.amount for t in rows if t.transaction_type == "income"), Decimal("0"))), "expenses": float(sum((t.amount for t in rows if t.transaction_type == "expense"), Decimal("0")))})


@bp.get("/export.csv")
def export_csv():
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["Descrição", "Valor", "Tipo", "Categoria", "Vencimento", "Status"])
    for item in filtered_transactions().all():
        writer.writerow([item.description, item.amount, item.transaction_type, item.category, item.due_date, item.status])
    response = make_response(output.getvalue())
    response.headers["Content-Disposition"] = "attachment; filename=lancamentos.csv"
    response.headers["Content-Type"] = "text/csv; charset=utf-8"
    return response
