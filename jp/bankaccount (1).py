class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")

    def display_balance(self):
        print("Balance:", self.balance)


account = BankAccount(10000)

account.deposit(5000)
account.withdraw(3000)

account.display_balance()