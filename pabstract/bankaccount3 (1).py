from abc import ABC, abstractmethod

class BankAccount(ABC):

    def __init__(self, balance):
        self.balance = balance

    @abstractmethod
    def calculate_interest(self):
        pass

    def display_balance(self):
        print("Balance:", self.balance)


class SavingsAccount(BankAccount):

    def calculate_interest(self):
        print("Interest = 5%")


account = SavingsAccount(10000)

account.calculate_interest()
account.display_balance()