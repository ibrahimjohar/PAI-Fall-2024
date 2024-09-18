class Account:
    def __init__(self):
        self.__account_no = None
        self.__account_bal = None
        self.__security_code = None

    def initialize_account(self, account_no, account_bal, security_code):
        self.__account_no = account_no
        self.__account_bal = account_bal
        self.__security_code = security_code

    def print_account_details(self):
        print("Account Number:", self.__account_no)
        print("Account Balance:", self.__account_bal)
        print("Security Code:", self.__security_code)


account = Account()

account.initialize_account("123456789", 1000.0, "1234")

account.print_account_details()