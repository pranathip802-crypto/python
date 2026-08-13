class Laptop:
    def __init__(self, brand, ram, processor, storage, price):
        self.brand = brand
        self.ram = ram
        self.processor = processor
        self.storage = storage
        self.price = price

    def display(self):
        print("Brand:", self.brand)
        print("RAM:", self.ram)
        print("Processor:", self.processor)
        print("Storage:", self.storage)
        print("Price:", self.price)


laptop = Laptop(
    "Dell",
    "16GB",
    "Intel i7",
    "512GB SSD",
    75000
)

laptop.display()