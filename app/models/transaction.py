from dataclasses import dataclass
from datetime import datetime


@dataclass
class Transaction:
    description: str
    amount: int
    type: str
    category: str
    date: str
    id: int | None = None
    created_at: str | None = None

    @classmethod
    def from_row(cls, row):
        return cls(
            id=row["id"],
            description=row["description"],
            amount=row["amount"],
            type=row["type"],
            category=row["category"],
            date=row["date"],
            created_at=row["created_at"],
        )

    @property
    def amount_decimal(self):
        from decimal import Decimal
        return Decimal(self.amount) / Decimal("100")

    @property
    def formatted_amount(self) -> str:
        value = self.amount_decimal
        return f"R$ {value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

    @property
    def formatted_date(self) -> str:
        try:
            return datetime.strptime(self.date, "%Y-%m-%d").strftime("%d/%m/%Y")
        except ValueError:
            return self.date
