class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, name, price, quantity):
        self.products.append([name, price, quantity])

    def total(self):
        total = 0

        for product in self.products:
            total += product[1] * product[2]

        return total

    def display(self):
        for product in self.products:
            print(
                product[0],
                product[1],
                product[2]
            )


cart = ShoppingCart()

cart.add_product("Laptop", 50000, 1)
cart.add_product("Mouse", 500, 2)
cart.add_product("Keyboard", 1000, 1)

cart.display()

print("Total Bill:", cart.total())