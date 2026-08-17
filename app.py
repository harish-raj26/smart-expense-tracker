from datetime import datetime

from models.expense import Expense

from services.storage_services import (
    create_database,
    save_expense,
    get_all_expenses,
    get_expenses_by_category,
    get_expenses_by_month,
    update_expense,
    delete_expense
)


def display_expenses(expenses):
    if not expenses:
        print("\nNo expenses found.")
        return

    print("\n" + "-" * 75)
    print(
        f"{'ID':<5}"
        f"{'Amount':<12}"
        f"{'Category':<15}"
        f"{'Merchant':<20}"
        f"{'Date':<15}"
    )
    print("-" * 75)

    for expense in expenses:
        expense_id, amount, category, merchant, date = expense

        print(
            f"{expense_id:<5}"
            f"₹{amount:<11.2f}"
            f"{category:<15}"
            f"{merchant:<20}"
            f"{date:<15}"
        )

    print("-" * 75)


def get_valid_date(prompt):
    while True:
        date = input(prompt).strip()

        try:
            datetime.strptime(date, "%Y-%m-%d")
            return date
        except ValueError:
            print("Invalid date. Use YYYY-MM-DD.")


def get_positive_amount(prompt):
    while True:
        try:
            amount = float(input(prompt))

            if amount <= 0:
                print("Amount must be greater than 0.")
                continue

            return amount

        except ValueError:
            print("Please enter a valid amount.")


def get_valid_id(prompt):
    while True:
        try:
            expense_id = int(input(prompt))

            if expense_id <= 0:
                print("ID must be greater than 0.")
                continue

            return expense_id

        except ValueError:
            print("Please enter a valid ID.")


def add_expense():
    print("\n--- Add Expense ---")

    amount = get_positive_amount("Enter amount: ")

    category = input("Enter category: ").strip().capitalize()

    while not category:
        print("Category cannot be empty.")
        category = input("Enter category: ").strip().capitalize()

    merchant = input("Enter merchant: ").strip()

    date = get_valid_date(
        "Enter date (YYYY-MM-DD): "
    )

    expense = Expense(
        amount,
        category,
        merchant,
        date
    )

    save_expense(expense)

    print("\nExpense saved successfully!")


def view_expenses():
    print("\n--- All Expenses ---")

    expenses = get_all_expenses()

    display_expenses(expenses)


def show_total_expenses():
    print("\n--- Total Expenses ---")

    expenses = get_all_expenses()

    total = 0

    for expense in expenses:
        total += expense[1]

    print(f"Total expenses: ₹{total:.2f}")


def filter_by_category():
    print("\n--- Filter by Category ---")

    category = input(
        "Enter category: "
    ).strip().capitalize()

    expenses = get_expenses_by_category(category)

    display_expenses(expenses)


def category_summary():
    print("\n--- Category Spending Summary ---")

    expenses = get_all_expenses()

    if not expenses:
        print("No expenses found.")
        return

    summary = {}

    for expense in expenses:
        category = expense[2]
        amount = expense[1]

        if category in summary:
            summary[category] += amount
        else:
            summary[category] = amount

    print()

    for category, total in summary.items():
        print(f"{category:<20} ₹{total:.2f}")


def update_existing_expense():
    print("\n--- Update Expense ---")

    expenses = get_all_expenses()

    if not expenses:
        print("No expenses available to update.")
        return

    display_expenses(expenses)

    expense_id = get_valid_id(
        "\nEnter Expense ID to update: "
    )

    found = False

    for expense in expenses:
        if expense[0] == expense_id:
            found = True
            break

    if not found:
        print("Expense with the given ID does not exist.")
        return

    amount = get_positive_amount(
        "Enter new amount: "
    )

    category = input(
        "Enter new category: "
    ).strip().capitalize()

    while not category:
        print("Category cannot be empty.")
        category = input(
            "Enter new category: "
        ).strip().capitalize()

    merchant = input(
        "Enter new merchant: "
    ).strip()

    date = get_valid_date(
        "Enter new date (YYYY-MM-DD): "
    )

    success = update_expense(
        expense_id,
        amount,
        category,
        merchant,
        date
    )

    if success:
        print("\nExpense updated successfully!")
    else:
        print("\nExpense could not be updated.")


def delete_existing_expense():
    print("\n--- Delete Expense ---")

    expenses = get_all_expenses()

    if not expenses:
        print("No expenses available to delete.")
        return

    display_expenses(expenses)

    expense_id = get_valid_id(
        "\nEnter Expense ID to delete: "
    )

    success = delete_expense(expense_id)

    if success:
        print("\nExpense deleted successfully!")
    else:
        print("\nExpense with the given ID does not exist.")


def monthly_summary():
    print("\n--- Monthly Spending Summary ---")

    month = input(
        "Enter month (YYYY-MM): "
    ).strip()

    try:
        datetime.strptime(month, "%Y-%m")
    except ValueError:
        print("Invalid month. Use YYYY-MM.")
        return

    expenses = get_expenses_by_month(month)

    if not expenses:
        print(f"No expenses found for {month}.")
        return

    total = 0

    for expense in expenses:
        total += expense[1]

    print(f"\nTotal spending for {month}: ₹{total:.2f}")

    display_expenses(expenses)


def main():
    create_database()

    print("\n===================================")
    print("       SMART EXPENSE TRACKER")
    print("===================================")

    while True:

        print("\n1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. View Expenses by Category")
        print("5. Category Spending Summary")
        print("6. Update Expense")
        print("7. Delete Expense")
        print("8. Monthly Spending Summary")
        print("9. Exit")

        choice = input(
            "\nEnter your choice: "
        ).strip()

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            show_total_expenses()

        elif choice == "4":
            filter_by_category()

        elif choice == "5":
            category_summary()

        elif choice == "6":
            update_existing_expense()

        elif choice == "7":
            delete_existing_expense()

        elif choice == "8":
            monthly_summary()

        elif choice == "9":
            print("\nThank you for using Smart Expense Tracker!")
            break

        else:
            print("\nInvalid choice. Please enter 1-9.")


if __name__ == "__main__":
    main()