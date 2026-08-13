class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


employee1 = Employee("Rahul", 40000)

print("Name:", employee1.name)
print("Salary:", employee1.salary)