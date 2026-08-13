class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_salary(self):
        print("Salary:", self.salary)


e = Employee("Ravi", 50000)
e.display_salary()