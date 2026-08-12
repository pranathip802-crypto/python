from abc import ABC, abstractmethod

class Payment(ABC):

    def __init__(self, amount):
        self.amount = amount

    @abstractmethod
    def pay(self):
        pass

    def display_amount(self):
        print("Amount:", self.amount)


class UPI(Payment):

    def pay(self):
        print("Payment through UPI")


payment = UPI(1500)

payment.pay()
payment.display_amount()