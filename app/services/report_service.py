from pathlib import Path

from app.utils.formatters import format_currency


class ReportService:
    def __init__(self, transaction_service):
        self.transaction_service = transaction_service

    def get_summary(self):
        return self.transaction_service.get_summary()

    def print_summary(self):
        summary = self.get_summary()

        print("\n" + "=" * 40)
        print("          RESUMO FINANCEIRO")
        print("=" * 40)
        print(f"Total de receitas: {format_currency(summary['total_revenue'])}")
        print(f"Total de despesas: {format_currency(summary['total_expenses'])}")
        print(f"Saldo:             {format_currency(summary['balance'])}")
        print("=" * 40)

    def generate_charts(self, output_dir: Path) -> list[Path]:
        try:
            import matplotlib
            matplotlib.use("Agg")
            import matplotlib.pyplot as plt
        except ImportError as exc:
            raise RuntimeError(
                "Matplotlib não está instalado. Execute: pip install -r requirements.txt"
            ) from exc

        transactions = self.transaction_service.list_transactions()
        output_dir.mkdir(parents=True, exist_ok=True)

        revenue = sum(t.amount for t in transactions if t.type == "RECEITA")
        expenses = sum(t.amount for t in transactions if t.type == "DESPESA")

        generated = []

        fig, ax = plt.subplots(figsize=(7, 5))
        ax.bar(["Receitas", "Despesas"], [revenue / 100, expenses / 100])
        ax.set_title("Receitas x Despesas")
        ax.set_ylabel("Valor (R$)")
        fig.tight_layout()
        path = output_dir / "receitas_vs_despesas.png"
        fig.savefig(path, dpi=150)
        plt.close(fig)
        generated.append(path)

        categories = {}
        for transaction in transactions:
            if transaction.type == "DESPESA":
                categories[transaction.category] = (
                    categories.get(transaction.category, 0) + transaction.amount
                )

        fig, ax = plt.subplots(figsize=(8, 5))
        if categories:
            labels = list(categories.keys())
            values = [value / 100 for value in categories.values()]
            ax.bar(labels, values)
            ax.set_title("Despesas por categoria")
            ax.set_ylabel("Valor (R$)")
            ax.tick_params(axis="x", rotation=30)
        else:
            ax.text(0.5, 0.5, "Nenhuma despesa cadastrada", ha="center", va="center")
            ax.set_axis_off()

        fig.tight_layout()
        path = output_dir / "despesas_por_categoria.png"
        fig.savefig(path, dpi=150)
        plt.close(fig)
        generated.append(path)

        return generated
