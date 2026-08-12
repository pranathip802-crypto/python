from abc import ABC, abstractmethod

class Product(ABC):

    def __init__(self, name, price):
        self.name = name
        self.price = price

    @abstractmethod
    def calculate_discount(self):
        pass

    def display_product(self):
        print("Product:", self.name)
        print("Price:", self.price)


class Laptop(Product):

    def calculate_discount(self):
        return self.price * 0.10


laptop = Laptop("Laptop", 50000)

print("Discount:", laptop.calculate_discount())
laptop.display_product()