import pytest

from app.database import connection
from app.services.transaction_service import TransactionService


@pytest.fixture()
def service(tmp_path, monkeypatch):
    database_path = tmp_path / "test_finance.db"
    monkeypatch.setattr(connection, "DATABASE_PATH", database_path)
    monkeypatch.setattr(connection, "DATA_DIR", tmp_path)
    connection.initialize_database()
    return TransactionService()


def test_create_transaction(service):
    transaction_id = service.add_transaction(
        "Salário", "4000,00", "RECEITA", "Trabalho", "19/08/2026"
    )
    transactions = service.list_transactions()

    assert transaction_id == 1
    assert len(transactions) == 1
    assert transactions[0].description == "Salário"
    assert transactions[0].amount == 400000


def test_financial_summary(service):
    service.add_transaction(
        "Salário", "4000,00", "RECEITA", "Trabalho", "19/08/2026"
    )
    service.add_transaction(
        "Supermercado", "350,00", "DESPESA", "Alimentação", "19/08/2026"
    )

    summary = service.get_summary()

    assert summary["total_revenue"] == 400000
    assert summary["total_expenses"] == 35000
    assert summary["balance"] == 365000


def test_negative_balance(service):
    service.add_transaction(
        "Aluguel", "2000,00", "DESPESA", "Moradia", "19/08/2026"
    )

    summary = service.get_summary()

    assert summary["balance"] == -200000


def test_empty_summary(service):
    summary = service.get_summary()

    assert summary["total_revenue"] == 0
    assert summary["total_expenses"] == 0
    assert summary["balance"] == 0


def test_delete_transaction(service):
    transaction_id = service.add_transaction(
        "Cinema", "50,00", "DESPESA", "Lazer", "19/08/2026"
    )

    assert service.delete_transaction(transaction_id) is True
    assert service.list_transactions() == []


def test_filter_by_type_and_category(service):
    service.add_transaction(
        "Salário", "4000,00", "RECEITA", "Trabalho", "19/08/2026"
    )
    service.add_transaction(
        "Mercado", "300,00", "DESPESA", "Alimentação", "19/08/2026"
    )
    service.add_transaction(
        "Restaurante", "100,00", "DESPESA", "Alimentação", "18/08/2026"
    )

    result = service.filter_transactions(
        transaction_type="DESPESA",
        category="Alimentação",
        start_date="18/08/2026",
        end_date="19/08/2026",
    )

    assert len(result) == 2
    assert all(item.type == "DESPESA" for item in result)
