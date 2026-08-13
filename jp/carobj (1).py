class Car:
    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price


c1 = Car("Toyota", "Camry", 2024, 3000000)
c2 = Car("Honda", "City", 2023, 1500000)
c3 = Car("Hyundai", "Creta", 2024, 1800000)

for car in [c1, c2, c3]:
    print(car.brand, car.model, car.year, car.price)