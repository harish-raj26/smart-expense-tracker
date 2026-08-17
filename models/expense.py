class Expense:
    def __init__(self, amount, category, merchant, date):
        self.amount = amount
        self.category = category
        self.merchant = merchant
        self.date = date

    def __str__(self):
        return (
            f"{self.amount} | "
            f"{self.category} | "
            f"{self.merchant} | "
            f"{self.date}"
        )