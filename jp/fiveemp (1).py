class Employee:
    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary


e1 = Employee("Ravi", "IT", 50000)
e2 = Employee("Anil", "HR", 45000)
e3 = Employee("Priya", "Finance", 55000)
e4 = Employee("Kiran", "Sales", 40000)
e5 = Employee("Meena", "IT", 60000)

employees = [e1, e2, e3, e4, e5]

for e in employees:
    print(e.name, e.department, e.salary)