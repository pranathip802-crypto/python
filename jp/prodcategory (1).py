class Product:
    category = "Electronics"

    def __init__(self, name, price):
        self.name = name
        self.price = price


p1 = Product("Laptop", 60000)
p2 = Product("Mobile", 30000)
p3 = Product("Tablet", 20000)

print(p1.name, p1.category)
print(p2.name, p2.category)
print(p3.name, p3.category)