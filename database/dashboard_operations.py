from database.db import get_connection
from database.income_operations import get_total_income


def get_total_expenses():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT SUM(amount)
        FROM expenses
    """)

    total = cursor.fetchone()[0]

    conn.close()

    return total if total else 0


def get_recent_transactions():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            amount,
            category,
            description,
            date
        FROM expenses
        ORDER BY id DESC
        LIMIT 5
    """)

    data = cursor.fetchall()

    conn.close()

    return data


def get_category_expenses():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            category,
            SUM(amount)
        FROM expenses
        GROUP BY category
    """)

    data = cursor.fetchall()

    conn.close()

    return data


def get_highest_category():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            category,
            SUM(amount) AS total
        FROM expenses
        GROUP BY category
        ORDER BY total DESC
        LIMIT 1
    """)

    data = cursor.fetchone()

    conn.close()

    return data


def get_balance():

    total_income = get_total_income()
    total_expenses = get_total_expenses()

    return total_income - total_expenses


def get_dashboard_summary():

    total_income = get_total_income()
    total_expenses = get_total_expenses()
    balance = total_income - total_expenses

    return {
        "income": total_income,
        "expenses": total_expenses,
        "balance": balance,
        "savings": balance
    }
def get_financial_summary():

    summary = get_dashboard_summary()
    categories = get_category_expenses()

    text = f"""
Financial Summary

Total Income: ₹{summary['income']:.2f}
Total Expenses: ₹{summary['expenses']:.2f}
Balance: ₹{summary['balance']:.2f}

Category Breakdown:
"""

    for category, amount in categories:
        text += f"\n- {category}: ₹{amount:.2f}"

    return text