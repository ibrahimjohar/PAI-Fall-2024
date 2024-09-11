#name: ibrahim johar farooqi
#date: 11 september 2024
#lab: 04
#task: 6

class BankAccount:
    account_number = 0
    balance = 0.0
    date_of_opening = ""
    customer_name = ""

    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def check_balance(self):
        print(f"balance: ${self.balance}")


bankacc = BankAccount(23, 100, "23 May 2024", "ibrahim")

print("bank details:")
print(f"name: {bankacc.customer_name}")
print(f"date of opening: {bankacc.date_of_opening}")
print(f"account number: {bankacc.account_number}")
bankacc.check_balance()

print("deposit of $100:")
bankacc.deposit(100)
bankacc.check_balance()

print("withdraw of $50:")
bankacc.withdraw(50)
bankacc.check_balance()
