import sqlite3
from datetime import datetime
from pathlib import Path

from app.database.connection import get_connection
from app.models.transaction import Transaction
from app.utils.validators import (
    validate_amount,
    validate_date,
    validate_required_text,
    validate_transaction_type,
)


class TransactionService:
    """Regras de negócio e acesso às movimentações."""

    def add_transaction(
        self,
        description: str,
        amount: str | int,
        transaction_type: str,
        category: str,
        date: str,
    ) -> int:
        description = validate_required_text(description, "Descrição")
        category = validate_required_text(category, "Categoria")
        transaction_type = validate_transaction_type(transaction_type)

        amount_cents = (
            validate_amount(amount) if isinstance(amount, str) else int(amount)
        )
        if amount_cents <= 0:
            raise ValueError("O valor deve ser maior que zero.")

        date_iso = validate_date(date) if "/" in date else date

        try:
            with get_connection() as connection:
                cursor = connection.execute(
                    """
                    INSERT INTO transactions
                    (description, amount, type, category, date)
                    VALUES (?, ?, ?, ?, ?)
                    """,
                    (
                        description,
                        amount_cents,
                        transaction_type,
                        category,
                        date_iso,
                    ),
                )
                connection.commit()
                return cursor.lastrowid
        except sqlite3.Error as exc:
            raise RuntimeError(f"Erro ao salvar movimentação: {exc}") from exc

    def list_transactions(self):
        with get_connection() as connection:
            rows = connection.execute(
                """
                SELECT id, description, amount, type, category, date, created_at
                FROM transactions
                ORDER BY date DESC, id DESC
                """
            ).fetchall()
        return [Transaction.from_row(row) for row in rows]

    def delete_transaction(self, transaction_id: int) -> bool:
        with get_connection() as connection:
            cursor = connection.execute(
                "DELETE FROM transactions WHERE id = ?",
                (transaction_id,),
            )
            connection.commit()
            return cursor.rowcount > 0

    def get_summary(self) -> dict:
        with get_connection() as connection:
            row = connection.execute(
                """
                SELECT
                    COALESCE(SUM(CASE WHEN type = 'RECEITA' THEN amount ELSE 0 END), 0)
                        AS total_revenue,
                    COALESCE(SUM(CASE WHEN type = 'DESPESA' THEN amount ELSE 0 END), 0)
                        AS total_expenses
                FROM transactions
                """
            ).fetchone()

        total_revenue = int(row["total_revenue"])
        total_expenses = int(row["total_expenses"])

        return {
            "total_revenue": total_revenue,
            "total_expenses": total_expenses,
            "balance": total_revenue - total_expenses,
        }

    def filter_transactions(
        self,
        transaction_type: str | None = None,
        category: str | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
    ):
        query = """
            SELECT id, description, amount, type, category, date, created_at
            FROM transactions
            WHERE 1 = 1
        """
        params = []

        if transaction_type:
            transaction_type = validate_transaction_type(transaction_type)
            query += " AND type = ?"
            params.append(transaction_type)

        if category:
            query += " AND LOWER(category) = LOWER(?)"
            params.append(category.strip())

        if start_date:
            query += " AND date >= ?"
            params.append(validate_date(start_date) if "/" in start_date else start_date)

        if end_date:
            query += " AND date <= ?"
            params.append(validate_date(end_date) if "/" in end_date else end_date)

        query += " ORDER BY date DESC, id DESC"

        with get_connection() as connection:
            rows = connection.execute(query, params).fetchall()

        return [Transaction.from_row(row) for row in rows]

    def export_csv(self, output_path: Path) -> int:
        import csv

        transactions = self.list_transactions()
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with output_path.open("w", newline="", encoding="utf-8-sig") as file:
            writer = csv.writer(file)
            writer.writerow(
                ["id", "description", "amount", "type", "category", "date"]
            )

            for transaction in transactions:
                writer.writerow(
                    [
                        transaction.id,
                        transaction.description,
                        f"{transaction.amount_decimal:.2f}",
                        transaction.type,
                        transaction.category,
                        transaction.formatted_date,
                    ]
                )

        return len(transactions)
