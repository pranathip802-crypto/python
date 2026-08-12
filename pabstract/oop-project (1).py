from abc import ABC, abstractmethod


class Employee(ABC):

    company = "ABC Technologies"

    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    @abstractmethod
    def calculate_salary(self):
        pass

    def display_company(self):
        print("Company:", Employee.company)

    def display_details(self):
        print("Name:", self.name)
        print("Employee ID:", self.employee_id)


class FullTimeEmployee(Employee):

    def calculate_salary(self):
        return 60000


class PartTimeEmployee(Employee):

    def calculate_salary(self):
        return 30000


class ContractEmployee(Employee):

    def calculate_salary(self):
        return 40000


employees = [
    FullTimeEmployee("Rahul", 101),
    PartTimeEmployee("Amit", 102),
    ContractEmployee("Priya", 103)
]


for employee in employees:
    print("--------------------")
    employee.display_company()
    employee.display_details()
    print("Salary:", employee.calculate_salary())