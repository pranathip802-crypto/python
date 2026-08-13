class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "City")
car3 = Car("Hyundai", "Creta")

print(car1.brand, car1.model)
print(car2.brand, car2.model)
print(car3.brand, car3.model)