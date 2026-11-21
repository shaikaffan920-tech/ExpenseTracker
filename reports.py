from database import connect_db


def show_summary():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            transaction_type,
            SUM(amount)
        FROM transactions
        GROUP BY transaction_type
    """)

    results = cursor.fetchall()
    conn.close()

    income = 0
    expenses = 0

    for transaction_type, total in results:
        if transaction_type == "income":
            income = total or 0
        elif transaction_type == "expense":
            expenses = total or 0

    balance = income - expenses

    print("======FINANCILA SUMMARY======")
    print(f"Total Income   : Rs. {income:.2f}")
    print(f"Total Expenses : Rs. {expenses:.2f}")
    print(f"Remaining      : Rs. {balance:.2f}")
    print("===============================")


def monthly_report():
    month = input(
        "Enter month (YYYY-MM): "
    ).strip()

    import re

    if not re.fullmatch(r"\d{4}-\d{2}", month):
        print("Invalid month format!")
        return

    year, month_number = map(int, month.split("-"))

    if not 1 <= month_number <= 12:
        print("Invalid month!")
        return

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT transaction_type, SUM(amount)
        FROM transactions
        WHERE date LIKE ?
        GROUP BY transaction_type
    """, (month + "-%",))

    results = cursor.fetchall()
    conn.close()

    income = 0
    expenses = 0

    for transaction_type, total in results:
        if transaction_type == "income":
            income = total or 0
        elif transaction_type == "expense":
            expenses = total or 0

    print(f"\n--- Report for {month} ---")
    print(f"Income   : Rs. {income:.2f}")
    print(f"Expenses : Rs. {expenses:.2f}")
    print(f"Balance  : Rs. {income - expenses:.2f}")


def category_report():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT category, SUM(amount)
        FROM transactions
        WHERE transaction_type = 'expense'
        GROUP BY category
        ORDER BY SUM(amount) DESC
    """)

    results = cursor.fetchall()
    conn.close()

    print("\n--- Category-wise Expenses ---")

    if not results:
        print("No expense records found!")
        return

    for category, total in results:
        print(f"{category:<20} Rs. {total:.2f}")