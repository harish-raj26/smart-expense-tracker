
from services.storage_services import (create_database,save_expense,get_all_expenses,get_expenses_by_category)

create_database()

print("Database created successfully")

# saving into database
 
'''from models.expense import Expense
from services.storage_services import save_expense
expense1 = Expense(100, "Food", "McDonald's", "2024-06-01")
save_expense(expense1)
print("Expense saved successfully")'''
from models.expense import Expense


create_database()
while True:
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. total expenses")
    print("4. View Expenses by Category")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")
        merchant = input("Enter merchant: ")
        date = input("Enter date (YYYY-MM-DD): ")

        expense = Expense(amount, category, merchant, date)
        save_expense(expense)
        print("Expense saved successfully!")

    elif choice == "2":
        expenses = get_all_expenses()
        summary = {}
        for expense in expenses:
                category = expense[2]
                amount = expense[1]
                if category in summary:
                    summary[category] += amount
                else:
                    summary[category] = amount
        print("Expense Summary by Category:", summary) 
        
        
        
        """for expense in expenses:
            print("id:", expense[0])
            print("Amount:", expense[1])
            print("Category:", expense[2])
            print("Merchant:", expense[3])
            print("Date:", expense[4])
           """ 

    elif choice == "3":
        expenses = get_all_expenses()
        sum=0

        for i in range(len(expenses)):
            sum=sum+expenses[i][1]
        print("total expenses:",sum)
    

    elif choice == "4":
        category = input("Enter category: ").capitalize()
        expenses = get_expenses_by_category(category)
        if not expenses:
            print("No expenses found for this category.")
        else:
            for expense in expenses:
                print("id:", expense[0])
                print("Amount:", expense[1])
                print("Category:", expense[2])
                print("Merchant:", expense[3])
                print("Date:", expense[4])



    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")
