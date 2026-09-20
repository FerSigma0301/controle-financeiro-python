from datetime import date, datetime
from decimal import Decimal

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Transaction(db.Model):
    __tablename__ = "transactions"

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(160), nullable=False)
    amount = db.Column(db.Numeric(12, 2), nullable=False)
    transaction_type = db.Column(db.String(10), nullable=False)
    category = db.Column(db.String(80), nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(10), nullable=False, default="pending")
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "amount": float(self.amount),
            "type": self.transaction_type,
            "category": self.category,
            "due_date": self.due_date.isoformat(),
            "status": self.status,
        }

    @property
    def is_overdue(self):
        return self.status == "pending" and self.due_date < date.today()
