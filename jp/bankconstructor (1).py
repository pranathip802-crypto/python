class BankAccount:
    def __init__(self, holder, account_number, balance):
        self.holder = holder
        self.account_number = account_number
        self.balance = balance


account = BankAccount("Ravi", "123456", 25000)

print("Holder:", account.holder)
print("Account Number:", account.account_number)
print("Balance:", account.balance)