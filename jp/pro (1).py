class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def total_price(self, quantity):
        return self.price * quantity


product = Product("Laptop", 50000)

print("Total:", product.total_price(3))