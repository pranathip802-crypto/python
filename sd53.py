subject1 = {
    "Ravi": 80,
    "Priya": 90,
    "Asha": 75,
    "Kiran": 85
}

subject2 = {
    "Priya": 88,
    "Kiran": 92,
    "Arun": 70
}

students1 = set(subject1.keys())
students2 = set(subject2.keys())

common = students1.intersection(students2)

print("Students in both subjects:", common)