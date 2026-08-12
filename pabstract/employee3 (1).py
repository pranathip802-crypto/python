from abc import ABC, abstractmethod

class Employee(ABC):

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @abstractmethod
    def display_details(self):
        pass


class Manager(Employee):

    def display_details(self):
        print("Role: Manager")
        print("Name:", self.name)
        print("Salary:", self.salary)


class Developer(Employee):

    def display_details(self):
        print("Role: Developer")
        print("Name:", self.name)
        print("Salary:", self.salary)


class Tester(Employee):

    def display_details(self):
        print("Role: Tester")
        print("Name:", self.name)
        print("Salary:", self.salary)


manager = Manager("Rahul", 70000)
developer = Developer("Amit", 50000)
tester = Tester("Priya", 45000)

manager.display_details()
print()

developer.display_details()
print()

tester.display_details()