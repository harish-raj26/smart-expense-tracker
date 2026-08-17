import sqlite3
from pathlib import Path


DATABASE_DIR = Path("database")
DATABASE_FILE = DATABASE_DIR / "expenses.db"


def create_database():
    DATABASE_DIR.mkdir(exist_ok=True)

    connection = sqlite3.connect(DATABASE_FILE)
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
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO expenses
        (amount, category, merchant, date)
        VALUES (?, ?, ?, ?)
    """, (
        expense.amount,
        expense.category,
        expense.merchant,
        expense.date
    ))

    connection.commit()
    connection.close()


def get_all_expenses():
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, amount, category, merchant, date
        FROM expenses
        ORDER BY id
    """)

    expenses = cursor.fetchall()

    connection.close()

    return expenses


def get_expenses_by_category(category):
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, amount, category, merchant, date
        FROM expenses
        WHERE LOWER(category) = LOWER(?)
        ORDER BY id
    """, (category,))

    expenses = cursor.fetchall()

    connection.close()

    return expenses


def get_expenses_by_month(month):
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, amount, category, merchant, date
        FROM expenses
        WHERE date LIKE ?
        ORDER BY date, id
    """, (month + "%",))

    expenses = cursor.fetchall()

    connection.close()

    return expenses


def delete_expense(expense_id):
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()

    cursor.execute("""
        DELETE FROM expenses
        WHERE id = ?
    """, (expense_id,))

    deleted = cursor.rowcount

    connection.commit()
    connection.close()

    return deleted > 0


def update_expense(expense_id, amount, category, merchant, date):
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE expenses
        SET amount = ?,
            category = ?,
            merchant = ?,
            date = ?
        WHERE id = ?
    """, (
        amount,
        category,
        merchant,
        date,
        expense_id
    ))

    updated = cursor.rowcount

    connection.commit()
    connection.close()

    return updated > 0