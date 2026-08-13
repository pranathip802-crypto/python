class Laptop:
    def __init__(self, brand, ram, processor, price):
        self.brand = brand
        self.ram = ram
        self.processor = processor
        self.price = price


laptop = Laptop("Dell", "16GB", "Intel i7", 75000)

print("Brand:", laptop.brand)
print("RAM:", laptop.ram)
print("Processor:", laptop.processor)
print("Price:", laptop.price)