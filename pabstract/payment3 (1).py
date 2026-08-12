from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class UPI(Payment):
    def pay(self, amount):
        print("UPI Payment:", amount)


class CreditCard(Payment):
    def pay(self, amount):
        print("Credit Card Payment:", amount)


class NetBanking(Payment):
    def pay(self, amount):
        print("Net Banking Payment:", amount)


payments = [UPI(), CreditCard(), NetBanking()]

for payment in payments:
    payment.pay(1000)