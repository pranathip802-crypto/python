employees = {
    "Ravi": 45000,
    "Priya": 60000,
    "Asha": 75000,
    "Kiran": 48000
}

for employee, salary in employees.items():
    if salary > 50000:
        print(employee, ":", salary)