from abc import ABC, abstractmethod

class Employee(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_salary(self):
        pass

    def display_company(self):
        print("Company: ABC Technologies")


class Developer(Employee):

    def calculate_salary(self):
        print("Developer Salary = 50000")


developer = Developer("Rahul")

developer.calculate_salary()
developer.display_company()