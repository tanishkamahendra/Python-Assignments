class BankAccount:

    def __init__(self, account_number, balance=0.0):
        
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        
        if amount > 0:
            self.balance += amount
            print("Deposited:", amount)
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        
        if amount <= self.balance and amount > 0:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")

    def check_balance(self):
        
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)

account = BankAccount("123456789", 500)
account.check_balance()
account.deposit(200)
account.withdraw(100)
account.check_balance()