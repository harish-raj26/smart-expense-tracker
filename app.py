
from services.storage_services import (create_database,save_expense,get_all_expenses)

create_database()

print("Database created successfully")

# saving into database
 
'''from models.expense import Expense
from services.storage_services import save_expense
expense1 = Expense(100, "Food", "McDonald's", "2024-06-01")
save_expense(expense1)
print("Expense saved successfully")'''
from models.expense import Expense

expense1 = Expense(
    100,
    "Food",
    "McDonald's",
    "2024-06-01"
)

print(expense1.amount)
save_expense(expense1)
print("expense saved successfully")
print(get_all_expenses())