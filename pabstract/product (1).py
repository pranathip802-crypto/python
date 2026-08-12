from abc import ABC, abstractmethod

class Product(ABC):

    def __init__(self, product_name, price):
        self.product_name = product_name
        self.price = price

    @abstractmethod
    def calculate_discount(self):
        pass


class Electronics(Product):

    def calculate_discount(self):
        discount = self.price * 0.10
        print("Product:", self.product_name)
        print("Price:", self.price)
        print("Discount:", discount)
        print("Final Price:", self.price - discount)


class Clothing(Product):

    def calculate_discount(self):
        discount = self.price * 0.20
        print("Product:", self.product_name)
        print("Price:", self.price)
        print("Discount:", discount)
        print("Final Price:", self.price - discount)


laptop = Electronics("Laptop", 50000)
shirt = Clothing("Shirt", 2000)

laptop.calculate_discount()
print()

shirt.calculate_discount()