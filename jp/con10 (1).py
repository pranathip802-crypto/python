class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, name):
        self.employees.append(name)

    def remove_employee(self, name):
        if name in self.employees:
            self.employees.remove(name)
            print("Employee removed")
        else:
            print("Employee not found")

    def search_employee(self, name):
        if name in self.employees:
            print("Employee found")
        else:
            print("Employee not found")

    def display_employees(self):
        print("Employees:")

        for employee in self.employees:
            print(employee)


company = Company()

company.add_employee("Ravi")
company.add_employee("Priya")
company.add_employee("Anil")

company.display_employees()

company.search_employee("Priya")

company.remove_employee("Anil")

company.display_employees()