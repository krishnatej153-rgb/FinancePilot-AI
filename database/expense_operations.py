from database.db import get_connection


def add_expense(amount, category, description, date):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO expenses(amount,category,description,date)
    VALUES(?,?,?,?)
    """, (amount, category, description, date))

    conn.commit()
    conn.close()


def get_expenses():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM expenses")

    data = cursor.fetchall()

    conn.close()

    return data