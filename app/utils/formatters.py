from decimal import Decimal


def format_currency(cents: int) -> str:
    value = Decimal(cents) / Decimal("100")
    return f"R$ {value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def format_date(iso_date: str) -> str:
    from datetime import datetime
    return datetime.strptime(iso_date, "%Y-%m-%d").strftime("%d/%m/%Y")


def print_transactions(transactions) -> None:
    if not transactions:
        print("\nNenhuma movimentação encontrada.")
        return

    print("\n" + "=" * 92)
    print(f"{'ID':<5} {'DATA':<12} {'TIPO':<10} {'CATEGORIA':<18} {'VALOR':>16}  DESCRIÇÃO")
    print("=" * 92)

    for transaction in transactions:
        print(
            f"{transaction.id:<5} "
            f"{transaction.formatted_date:<12} "
            f"{transaction.type:<10} "
            f"{transaction.category[:18]:<18} "
            f"{transaction.formatted_amount:>16}  "
            f"{transaction.description}"
        )

    print("=" * 92)
