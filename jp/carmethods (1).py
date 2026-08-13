class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        print("Car started")

    def stop(self):
        print("Car stopped")

    def display_details(self):
        print("Brand:", self.brand)
        print("Model:", self.model)


car = Car("Toyota", "Camry")

car.start()
car.display_details()
car.stop()