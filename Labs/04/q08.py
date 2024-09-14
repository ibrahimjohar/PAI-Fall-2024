#name: ibrahim johar farooqi
#date: 11 september 2024
#lab: 04
#task: 8

class Account:
    def __init__(self, account_no, account_bal, security_code):
        self.__account_no = account_no
        self.__account_bal = account_bal
        self.__security_code = security_code
    
    def print_info(self):
        print(f"account number: {self.__account_no}")
        print(f"account balance: ${self.__account_bal}")
        print(f"security code: {self.__security_code}")


acc = Account(4356721,17500.75,9076)
acc.print_info()
