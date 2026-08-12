

from abc import ABC, abstractmethod

class Vehicle(ABC):

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):

    def start(self):
        print(self.brand, self.model, "starts")

    def stop(self):
        print(self.brand, self.model, "stops")


class Bike(Vehicle):

    def start(self):
        print(self.brand, self.model, "starts")

    def stop(self):
        print(self.brand, self.model, "stops")


car = Car("Toyota", "Camry")
bike = Bike("Honda", "CBR")

print(car.brand, car.model)
car.start()
car.stop()

print()

print(bike.brand, bike.model)
bike.start()
bike.stop()