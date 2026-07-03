from database.db import get_connection


def get_total_expenses():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT SUM(amount) FROM expenses"
    )

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