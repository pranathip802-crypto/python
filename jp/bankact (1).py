class BankAccount:
    def __init__(self, holder_name, account_number):
        self.holder_name = holder_name
        self.account_number = account_number


account = BankAccount("Ravi", "123456789")

print("Account Holder:", account.holder_name)
print("Account Number:", account.account_number)