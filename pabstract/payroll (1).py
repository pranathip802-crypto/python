from abc import ABC, abstractmethod

class EmployeePayroll(ABC):

    @abstractmethod
    def calculate_salary(self):
        pass


class FullTimeEmployee(EmployeePayroll):

    def calculate_salary(self):
        print("Full-Time Salary = 60000")


class PartTimeEmployee(EmployeePayroll):

    def calculate_salary(self):
        print("Part-Time Salary = 30000")


class ContractEmployee(EmployeePayroll):

    def calculate_salary(self):
        print("Contract Salary = 40000")


employees = [
    FullTimeEmployee(),
    PartTimeEmployee(),
    ContractEmployee()
]

for employee in employees:
    employee.calculate_salary()