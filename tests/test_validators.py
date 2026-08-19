import pytest

from app.utils.validators import (
    validate_amount,
    validate_date,
    validate_transaction_type,
)


def test_validate_amount_valid():
    assert validate_amount("10,50") == 1050


def test_validate_amount_rejects_invalid_value():
    with pytest.raises(ValueError):
        validate_amount("abc")


def test_validate_amount_rejects_zero():
    with pytest.raises(ValueError):
        validate_amount("0")


def test_validate_date_valid():
    assert validate_date("19/08/2026") == "2026-08-19"


def test_validate_date_invalid():
    with pytest.raises(ValueError):
        validate_date("99/99/2026")


def test_validate_transaction_type_valid():
    assert validate_transaction_type("receita") == "RECEITA"


def test_validate_transaction_type_invalid():
    with pytest.raises(ValueError):
        validate_transaction_type("INVÁLIDO")
