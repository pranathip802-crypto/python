marks = {
    "Ravi": 85,
    "Priya": 92,
    "Asha": 78,
    "Kiran": 88
}

highest = None
topper = ""

for student, mark in marks.items():
    if highest is None or mark > highest:
        highest = mark
        topper = student

print("Topper:", topper)
print("Marks:", highest)