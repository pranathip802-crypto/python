from abc import ABC, abstractmethod

class Vehicle(ABC):

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    @abstractmethod
    def start(self):
        pass

    def display_info(self):
        print("Brand:", self.brand)
        print("Model:", self.model)


class Car(Vehicle):

    def start(self):
        print("Car started")


car = Car("Toyota", "Camry")

car.start()
car.display_info()