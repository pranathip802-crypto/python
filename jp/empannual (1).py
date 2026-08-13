class Employee:
    def __init__(self, monthly_salary):
        self.monthly_salary = monthly_salary

    def annual_salary(self):
        return self.monthly_salary * 12


employee = Employee(50000)

print("Annual Salary:", employee.annual_salary())