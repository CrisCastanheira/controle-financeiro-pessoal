from app.cli.menu import Menu
from app.database.connection import initialize_database


def main():
    initialize_database()
    Menu().run()


if __name__ == "__main__":
    main()
