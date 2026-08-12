from abc import ABC, abstractmethod

class Vehicle(ABC):

    def __init__(self, vehicle_number):
        self.vehicle_number = vehicle_number

    @abstractmethod
    def rent(self, days):
        pass


class Car(Vehicle):

    def rent(self, days):
        print("Car Rental =", days * 1000)


class Bike(Vehicle):

    def rent(self, days):
        print("Bike Rental =", days * 500)


class Bus(Vehicle):

    def rent(self, days):
        print("Bus Rental =", days * 2000)


vehicles = [
    Car("CAR101"),
    Bike("BIKE202"),
    Bus("BUS303")
]

for vehicle in vehicles:
    vehicle.rent(3)