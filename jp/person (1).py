class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city


p1 = Person("Ravi", 25, "Hyderabad")
p2 = Person("Priya", 23, "Vijayawada")

print(p1.name, p1.age, p1.city)
print(p2.name, p2.age, p2.city)