marks = {
    "Ravi": 85,
    "Priya": 95,
    "Asha": 72,
    "Kiran": 88,
    "Arun": 65
}

highest = None
lowest = None
topper = ""
lowest_student = ""

for student, mark in marks.items():

    if highest is None or mark > highest:
        highest = mark
        topper = student

    if lowest is None or mark < lowest:
        lowest = mark
        lowest_student = student

print("Topper:", topper, highest)
print("Lowest scorer:", lowest_student, lowest)