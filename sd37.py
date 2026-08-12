employees = {
    "Ravi": 40000,
    "Priya": 50000,
    "Asha": 60000,
    "Kiran": 45000
}

total = 0

for salary in employees.values():
    total += salary

average = total / len(employees)

print("Average salary:", average)