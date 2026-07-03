from database.db import get_connection


def get_total_expenses():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT SUM(amount) FROM expenses")

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
        SELECT category, SUM(amount)
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
        SELECT category, SUM(amount) AS total
        FROM expenses
        GROUP BY category
        ORDER BY total DESC
        LIMIT 1
    """)

    data = cursor.fetchone()

    conn.close()

    return data