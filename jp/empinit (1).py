class Employee:
    def __init__(self, employee_id, name, department, salary):
        self.employee_id = employee_id
        self.name = name
        self.department = department
        self.salary = salary


employee = Employee(101, "Ravi", "IT", 50000)

print(employee.employee_id)
print(employee.name)
print(employee.department)
print(employee.salary)