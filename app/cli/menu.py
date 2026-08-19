from datetime import datetime
from pathlib import Path

from app.services.report_service import ReportService
from app.services.transaction_service import TransactionService
from app.utils.formatters import format_currency, print_transactions
from app.utils.validators import validate_date


class Menu:
    def __init__(self):
        self.transaction_service = TransactionService()
        self.report_service = ReportService(self.transaction_service)
        self.base_dir = Path(__file__).resolve().parents[2]
        self.exports_dir = self.base_dir / "exports"

    def run(self):
        while True:
            self._print_menu()
            option = input("Escolha uma opção: ").strip()

            try:
                if option == "1":
                    self._add_transaction("RECEITA")
                elif option == "2":
                    self._add_transaction("DESPESA")
                elif option == "3":
                    self._list_transactions()
                elif option == "4":
                    self.report_service.print_summary()
                elif option == "5":
                    self._filter_transactions()
                elif option == "6":
                    self._export_csv()
                elif option == "7":
                    self._generate_charts()
                elif option == "8":
                    self._delete_transaction()
                elif option == "0":
                    print("\nAté logo!")
                    break
                else:
                    print("\nOpção inválida.")
            except (ValueError, RuntimeError) as exc:
                print(f"\nErro: {exc}")

            if option != "0":
                input("\nPressione ENTER para continuar...")

    @staticmethod
    def _print_menu():
        print("\n" + "=" * 40)
        print("      CONTROLE FINANCEIRO PESSOAL")
        print("=" * 40)
        print("1. Adicionar receita")
        print("2. Adicionar despesa")
        print("3. Listar movimentações")
        print("4. Consultar resumo financeiro")
        print("5. Filtrar movimentações")
        print("6. Exportar dados para CSV")
        print("7. Gerar gráfico")
        print("8. Excluir movimentação")
        print("0. Sair")
        print("=" * 40)

    def _add_transaction(self, transaction_type: str):
        print(f"\n--- Nova {transaction_type.lower()} ---")
        description = input("Descrição: ")
        amount = input("Valor: ")
        category = input("Categoria: ")
        date = input("Data (DD/MM/AAAA): ")

        transaction_id = self.transaction_service.add_transaction(
            description, amount, transaction_type, category, date
        )

        print(f"\nMovimentação #{transaction_id} cadastrada com sucesso!")

    def _list_transactions(self):
        transactions = self.transaction_service.list_transactions()
        print_transactions(transactions)

    def _filter_transactions(self):
        print("\n--- FILTROS ---")
        print("Deixe em branco o filtro que não quiser utilizar.")
        transaction_type = input("Tipo (RECEITA/DESPESA): ").strip() or None
        category = input("Categoria: ").strip() or None
        start_date = input("Data inicial (DD/MM/AAAA): ").strip() or None
        end_date = input("Data final (DD/MM/AAAA): ").strip() or None

        if start_date and end_date:
            if validate_date(start_date) > validate_date(end_date):
                raise ValueError("A data inicial não pode ser maior que a data final.")

        transactions = self.transaction_service.filter_transactions(
            transaction_type=transaction_type,
            category=category,
            start_date=start_date,
            end_date=end_date,
        )
        print_transactions(transactions)

    def _export_csv(self):
        output_path = self.exports_dir / "transactions.csv"
        count = self.transaction_service.export_csv(output_path)
        print(f"\nCSV exportado com sucesso: {output_path}")
        print(f"Movimentações exportadas: {count}")

    def _generate_charts(self):
        generated = self.report_service.generate_charts(self.exports_dir)
        print("\nGráficos gerados com sucesso:")
        for path in generated:
            print(f"- {path}")

    def _delete_transaction(self):
        transactions = self.transaction_service.list_transactions()
        print_transactions(transactions)

        if not transactions:
            return

        raw_id = input("\nDigite o ID da movimentação que deseja excluir: ").strip()
        try:
            transaction_id = int(raw_id)
        except ValueError as exc:
            raise ValueError("ID inválido. Digite um número inteiro.") from exc

        transaction = next(
            (item for item in transactions if item.id == transaction_id),
            None,
        )

        if transaction is None:
            print("\nMovimentação não encontrada.")
            return

        print(
            f"\nVocê selecionou: {transaction.description} "
            f"({format_currency(transaction.amount)})"
        )
        confirmation = input(
            "Tem certeza que deseja excluir esta movimentação? (s/n): "
        ).strip().lower()

        if confirmation != "s":
            print("\nExclusão cancelada.")
            return

        deleted = self.transaction_service.delete_transaction(transaction_id)

        if deleted:
            print("\nMovimentação excluída com sucesso.")
        else:
            print("\nMovimentação não encontrada.")
