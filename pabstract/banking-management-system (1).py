from abc import ABC, abstractmethod

class Account(ABC):

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")

    @abstractmethod
    def account_type(self):
        pass


class SavingsAccount(Account):

    def account_type(self):
        print("Account Type: Savings")


class CurrentAccount(Account):

    def account_type(self):
        print("Account Type: Current")


account = SavingsAccount("Rahul", 10000)

print("Name:", account.name)
account.account_type()
account.deposit(2000)
account.withdraw(3000)
print("Balance:", account.balance)