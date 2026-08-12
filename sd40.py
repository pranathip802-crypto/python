marks = {
    "Ravi": 80,
    "Priya": 72,
    "Asha": 90,
    "Kiran": 65
}

for student, mark in marks.items():
    if mark > 75:
        print(student, ":", mark)