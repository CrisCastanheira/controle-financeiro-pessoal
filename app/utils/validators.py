from datetime import datetime
from decimal import Decimal, InvalidOperation


VALID_TYPES = ("RECEITA", "DESPESA")


def validate_amount(value: str) -> int:
    """Converte um valor monetário em centavos, evitando float."""
    cleaned = value.strip().replace("R$", "").replace(" ", "")

    if not cleaned:
        raise ValueError("Valor inválido. Digite um número válido.")

    # Aceita formatos como 10,50 / 10.50 / 1.999,99 / 1999.99
    if "," in cleaned and "." in cleaned:
        cleaned = cleaned.replace(".", "").replace(",", ".")
    elif "," in cleaned:
        cleaned = cleaned.replace(",", ".")
    elif cleaned.count(".") > 1:
        cleaned = cleaned.replace(".", "")
    elif "." in cleaned:
        parts = cleaned.split(".")
        if len(parts[-1]) == 3:
            cleaned = "".join(parts)

    try:
        amount = Decimal(cleaned)
    except InvalidOperation as exc:
        raise ValueError("Valor inválido. Digite um número válido.") from exc

    if amount <= 0:
        raise ValueError("O valor deve ser maior que zero.")

    if amount.as_tuple().exponent < -2:
        raise ValueError("O valor pode ter no máximo duas casas decimais.")

    cents = int(amount * 100)

    if cents <= 0:
        raise ValueError("O valor deve ser maior que zero.")

    return cents


def validate_date(value: str) -> str:
    """Valida DD/MM/AAAA e retorna no padrão ISO usado no banco."""
    try:
        parsed = datetime.strptime(value.strip(), "%d/%m/%Y")
    except ValueError as exc:
        raise ValueError("Data inválida. Utilize DD/MM/AAAA.") from exc

    return parsed.strftime("%Y-%m-%d")


def validate_transaction_type(value: str) -> str:
    normalized = value.strip().upper()
    if normalized not in VALID_TYPES:
        raise ValueError("Tipo inválido. Utilize RECEITA ou DESPESA.")
    return normalized


def validate_required_text(value: str, field_name: str) -> str:
    value = value.strip()
    if not value:
        raise ValueError(f"{field_name} é obrigatório.")
    return value
