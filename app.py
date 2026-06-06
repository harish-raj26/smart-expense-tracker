 #print("hello expense tracker")

expense =[]

amt =int(input("enter amount spent:"))
category =input("enter category of expense:")

print("AMOUNT:",amt)
print("CATEGORY:",category)

expenses={
    "amount":amt,
    "category":category
}

expense.append(expenses)
print("EXPENSES:",expense)