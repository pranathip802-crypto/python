from abc import ABC, abstractmethod

class Delivery(ABC):

    @abstractmethod
    def deliver(self):
        pass


class BikeDelivery(Delivery):

    def deliver(self):
        print("Food delivered by Bike")


class CarDelivery(Delivery):

    def deliver(self):
        print("Food delivered by Car")


class ExpressDelivery(Delivery):

    def deliver(self):
        print("Food delivered by Express Service")


deliveries = [
    BikeDelivery(),
    CarDelivery(),
    ExpressDelivery()
]

for delivery in deliveries:
    delivery.deliver()
    