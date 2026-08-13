class Car:
    company = "Toyota"
    number_of_wheels = 4

    def __init__(self, model, price):
        self.model = model
        self.price = price


c1 = Car("Camry", 3000000)
c2 = Car("Fortuner", 4000000)

print(c1.company, c1.number_of_wheels, c1.model, c1.price)
print(c2.company, c2.number_of_wheels, c2.model, c2.price)