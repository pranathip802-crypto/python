class Product:
    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity

    def total_cost(self):
        return self.price * self.quantity


product = Product(500, 4)

print("Total Cost:", product.total_cost())