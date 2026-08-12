from abc import ABC, abstractmethod

class Employee(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def salary(self):
        pass


class FullTimeEmployee(Employee):

    def salary(self):
        return 60000


class PartTimeEmployee(Employee):

    def salary(self):
        return 30000


class ContractEmployee(Employee):

    def salary(self):
        return 40000


employees = [
    FullTimeEmployee("Rahul"),
    PartTimeEmployee("Amit"),
    ContractEmployee("Priya")
]

for employee in employees:
    print(employee.name, "Salary =", employee.salary())