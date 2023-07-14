class Account:
    def __init__(self, acc_no, acc_name, acc_type, balance=0):
        self.acc_no = acc_no
        self.acc_name = acc_name
        self.acc_type = acc_type
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount

    def check_balance(self):
        return self.balance


class Bank:
    def __init__(self, bank_name):
        self.bank_name = bank_name
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def remove_account(self, account):
        self.accounts.remove(account)

    def display_accounts(self):
        for account in self.accounts:
            print("Account Number:", account.acc_no)
            print("Account Holder Name:", account.acc_name)
            print("Account Type:", account.acc_type)
            print("Balance:", account.balance)


bank = Bank("My Bank")
account1 = Account("A001", "Rince", "Savings")
account2 = Account("A002", "Rinu", "Checking")
bank.add_account(account1)
bank.add_account(account2)

bank.display_accounts()


account1.deposit(1000)
account2.deposit(500)
account1.withdraw(500)
account2.withdraw(1000)

bank.display_accounts()
