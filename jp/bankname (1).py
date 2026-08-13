class BankAccount:
    bank_name = "State Bank"

    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance


a1 = BankAccount("Ravi", 50000)
a2 = BankAccount("Priya", 70000)

print(a1.holder, a1.bank_name)
print(a2.holder, a2.bank_name)