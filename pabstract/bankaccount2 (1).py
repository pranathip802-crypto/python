from abc import ABC, abstractmethod

class BankAccount(ABC):

    def __init__(self, account_holder, account_number):
        self.account_holder = account_holder
        self.account_number = account_number

    @abstractmethod
    def calculate_interest(self):
        pass


class SavingsAccount(BankAccount):

    def calculate_interest(self):
        print("Savings Account Interest = 5%")


class CurrentAccount(BankAccount):

    def calculate_interest(self):
        print("Current Account Interest = 2%")


savings = SavingsAccount("Rahul", "SB1001")
current = CurrentAccount("Priya", "CA2001")

print("Account Holder:", savings.account_holder)
print("Account Number:", savings.account_number)
savings.calculate_interest()

print()

print("Account Holder:", current.account_holder)
print("Account Number:", current.account_number)
current.calculate_interest()