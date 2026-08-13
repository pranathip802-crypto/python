class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity


p1 = Product("Pen", 10, 5)
p2 = Product("Book", 100, 3)
p3 = Product("Bag", 500, 2)

print(p1.name, p1.total_price())
print(p2.name, p2.total_price())
print(p3.name, p3.total_price())