# Controle Financeiro

Aplicação web para organizar receitas, despesas e acompanhar o saldo mensal.

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.1-000000?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![SQLite](https://img.shields.io/badge/SQLite-3-003B57?logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![Status](https://img.shields.io/badge/status-em%20desenvolvimento-orange)](#roadmap)

## Sobre o projeto

Dashboard financeiro de portfólio com interface web responsiva para registrar lançamentos e visualizar receitas, despesas e saldo.

## Funcionalidades

- Cadastro de receitas e despesas
- Categorias e datas de vencimento
- Status pago ou pendente
- Filtros por período, tipo e status
- Resumo de receitas, despesas e saldo
- Gráfico de resumo com Chart.js
- Exportação dos lançamentos para CSV
- Interface web responsiva

> A exportação para Excel está planejada para uma próxima versão; a exportação atualmente disponível é CSV.

## Tecnologias

| Tecnologia | Uso |
|---|---|
| Python | Linguagem principal |
| Flask | Aplicação web e rotas |
| SQLite | Banco de dados local |
| Flask-SQLAlchemy | ORM e persistência |
| Chart.js | Gráfico do dashboard |
| Pandas e OpenPyXL | Planejados para relatórios e Excel |

## Como executar

```bash
git clone -b feature/financeiro-inicial https://github.com/FerSigma0301/controle-financeiro-python.git
cd controle-financeiro-python
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

```bash
pip install -r requirements.txt
python run.py
```

Acesse `http://127.0.0.1:5000`.

## Rotas principais

| Método | Rota | Descrição |
|---|---|---|
| GET | `/` | Exibe o dashboard |
| POST | `/transactions` | Cria um lançamento |
| POST | `/transactions/{id}/delete` | Exclui um lançamento |
| GET | `/api/summary` | Retorna o resumo em JSON |
| GET | `/export.csv` | Exporta lançamentos filtrados para CSV |

## Exemplo de lançamento

```text
Descrição: Mercado
Valor: 250,00
Tipo: Despesa
Categoria: Alimentação
Vencimento: 2026-09-30
Status: Pendente
```

## Estrutura

```text
app/
├── __init__.py
├── models.py
├── routes.py
└── templates/
    └── dashboard.html

run.py
requirements.txt
```

## Roadmap

- [ ] Exportação para Excel
- [ ] Relatório mensal detalhado
- [ ] Edição de lançamentos
- [ ] Autenticação de usuários
- [ ] Testes automatizados
- [ ] Docker e deploy

## Licença

Este projeto está sob a licença MIT.
