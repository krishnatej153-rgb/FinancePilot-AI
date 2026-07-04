from database.db import get_connection


def add_income(amount, source, description, date):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO income(
            amount,
            source,
            description,
            date
        )
        VALUES (?, ?, ?, ?)
    """, (amount, source, description, date))

    conn.commit()
    conn.close()


def get_income():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM income
        ORDER BY id DESC
    """)

    data = cursor.fetchall()

    conn.close()

    return data


def get_total_income():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT SUM(amount)
        FROM income
    """)

    total = cursor.fetchone()[0]

    conn.close()

    return total if total else 0


def delete_income(income_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM income
        WHERE id = ?
    """, (income_id,))

    conn.commit()
    conn.close()