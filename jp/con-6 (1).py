class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal successful")
        else:
            print("Insufficient balance")

    def display_balance(self):
        print("Balance:", self.balance)


account = BankAccount(10000)

account.withdraw(3000)
account.display_balance()

account.withdraw(10000)
account.display_balance()