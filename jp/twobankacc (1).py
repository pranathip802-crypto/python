class BankAccount:
    def __init__(self, account_holder, account_number, balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance


a1 = BankAccount("Ravi", "1001", 50000)
a2 = BankAccount("Priya", "1002", 75000)

print(a1.account_holder, a1.account_number, a1.balance)
print(a2.account_holder, a2.account_number, a2.balance)