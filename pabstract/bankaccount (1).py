
from abc import ABC, abstractmethod

class BankAccount(ABC):

    @abstractmethod
    def calculate_interest(self):
        pass


class SavingsAccount(BankAccount):
    def calculate_interest(self):
        balance = 10000
        rate = 5
        interest = balance * rate / 100

        print("Savings Account Interest =", interest)


class CurrentAccount(BankAccount):
    def calculate_interest(self):
        balance = 10000
        rate = 2
        interest = balance * rate / 100

        print("Current Account Interest =", interest)


savings = SavingsAccount()
current = CurrentAccount()

savings.calculate_interest()
current.calculate_interest()