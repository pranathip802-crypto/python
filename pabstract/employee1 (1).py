from abc import ABC, abstractmethod

class Employee(ABC):

    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    @abstractmethod
    def calculate_salary(self):
        pass


class Developer(Employee):

    def calculate_salary(self):
        print("Developer Salary = 50000")


class Manager(Employee):

    def calculate_salary(self):
        print("Manager Salary = 70000")


developer = Developer("Rahul", 101)
manager = Manager("Priya", 102)

print("Name:", developer.name)
print("Employee ID:", developer.employee_id)
developer.calculate_salary()

print()

print("Name:", manager.name)
print("Employee ID:", manager.employee_id)
manager.calculate_salary()