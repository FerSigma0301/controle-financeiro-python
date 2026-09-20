# Controle Financeiro

Aplicação web para organizar receitas, despesas e acompanhar o saldo mensal.

## Funcionalidades

- Cadastro de receitas e despesas
- Categorias e datas de vencimento
- Status pago ou pendente
- Filtros por período, tipo, categoria e status
- Resumo de receitas, despesas e saldo
- Gráfico mensal de gastos
- Exportação para CSV e Excel

## Tecnologias

Python, Flask, SQLite, SQLAlchemy, Pandas, OpenPyXL e Chart.js.

## Executar

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
python run.py
```

Acesse `http://127.0.0.1:5000`.
