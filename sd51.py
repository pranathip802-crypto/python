students = [
    "Ravi", "Priya", "Ravi",
    "Asha", "Priya", "Ravi"
]

frequency = {}

for student in students:
    if student in frequency:
        frequency[student] += 1
    else:
        frequency[student] = 1

print(frequency)