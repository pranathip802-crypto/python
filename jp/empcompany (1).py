class Employee:
    company_name = "Tech Solutions"

    def __init__(self, name):
        self.name = name


e1 = Employee("Ravi")
e2 = Employee("Priya")
e3 = Employee("Anil")

print(e1.name, e1.company_name)
print(e2.name, e2.company_name)
print(e3.name, e3.company_name)