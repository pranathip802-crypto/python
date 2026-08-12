employees = {
    "Ravi": "IT",
    "Priya": "HR",
    "Asha": "IT",
    "Kiran": "Finance",
    "Arun": "HR"
}

departments = set()

for department in employees.values():
    departments.add(department)

print("Unique departments:", departments)