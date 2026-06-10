import sqlite3


def create_database():
    connection = sqlite3.connect("database/expenses.db")

    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        amount REAL NOT NULL,
        category TEXT NOT NULL,
        merchant TEXT,
        date TEXT NOT NULL
    )
    """)

    connection.commit()
    connection.close()

def save_expense(expense):
    connection = sqlite3.connect("database/expenses.db")
    cursor = connection.cursor()
    cursor.execute("""INSERT INTO expenses (amount, category, merchant, date) VALUES (?, ?, ?, ?)""", 
    (expense.amount, expense.category, expense.merchant, expense.date))

    connection.commit()
    connection.close()

def get_all_expenses():
    connection = sqlite3.connect("database/expenses.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM expenses")

    expenses = cursor.fetchall()


    connection.close()

    return expenses