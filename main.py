print("Expense Tracker is Starting")
import sys
from pathlib import Path

# Ensure local project modules are importable when launched from another directory.
sys.path.insert(0, str(Path(__file__).resolve().parent))

from database import create_table

from expenses import (
    add_transaction,
    view_transactions,
    update_transaction,
    delete_transaction
)

from reports import (
    show_summary,
    monthly_report,
    category_report
)


def main():
    print("main function is working")

    create_table()

    while True:

        print("\n")
        print("=" * 40)
        print("PERSONAL EXPENSE TRACKER")
        print("=" * 40)

        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Update Transaction")
        print("4. Delete Transaction")
        print("5. Financial Summary")
        print("6. Monthly Report")
        print("7. Category-wise Report")
        print("8. Exit")

        print("=" * 40)

        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            add_transaction()

        elif choice == "2":
            view_transactions()

        elif choice == "3":
            update_transaction()

        elif choice == "4":
            delete_transaction()

        elif choice == "5":
            show_summary()

        elif choice == "6":
            monthly_report()

        elif choice == "7":
            category_report()

        elif choice == "8":
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice! Please try again.")
if __name__ == "__main__":
    print("Calling main function... ")
    main()
    

