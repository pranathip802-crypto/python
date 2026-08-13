class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, name, price, quantity):
        self.products.append({
            "name": name,
            "price": price,
            "quantity": quantity
        })

    def remove_product(self, name):
        for product in self.products:
            if product["name"] == name:
                self.products.remove(product)
                return

    def total(self):
        total = 0

        for product in self.products:
            total += product["price"] * product["quantity"]

        return total


cart = ShoppingCart()

cart.add_product("Laptop", 50000, 1)
cart.add_product("Mouse", 500, 2)

print("Total:", cart.total())

cart.remove_product("Mouse")

print("Total after removal:", cart.total())