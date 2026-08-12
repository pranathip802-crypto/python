from abc import ABC, abstractmethod

class Payment(ABC):

    def __init__(self, amount):
        self.amount = amount

    @abstractmethod
    def process_payment(self):
        pass


class UPI(Payment):

    def process_payment(self):
        print("UPI payment:", self.amount)


class CreditCard(Payment):

    def process_payment(self):
        print("Credit Card payment:", self.amount)


class DebitCard(Payment):

    def process_payment(self):
        print("Debit Card payment:", self.amount)


class NetBanking(Payment):

    def process_payment(self):
        print("Net Banking payment:", self.amount)


payments = [
    UPI(1000),
    CreditCard(2000),
    DebitCard(3000),
    NetBanking(4000)
]

for payment in payments:
    payment.process_payment()