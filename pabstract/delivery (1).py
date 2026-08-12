from abc import ABC, abstractmethod

class Delivery(ABC):

    @abstractmethod
    def calculate_charge(self):
        pass

    @abstractmethod
    def deliver(self):
        pass


class StandardDelivery(Delivery):

    def calculate_charge(self):
        print("Standard Delivery Charge = 50")

    def deliver(self):
        print("Product delivered using Standard Delivery")


class ExpressDelivery(Delivery):

    def calculate_charge(self):
        print("Express Delivery Charge = 100")

    def deliver(self):
        print("Product delivered using Express Delivery")


standard = StandardDelivery()
express = ExpressDelivery()

standard.calculate_charge()
standard.deliver()

express.calculate_charge()
express.deliver()