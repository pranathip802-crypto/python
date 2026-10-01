students = [
    {"name": "Sai", "marks": 90, "course": "CSE"},
    {"name": "Joy", "marks": 75, "course": "CSE"},
    {"name": "Sri", "marks": 85, "course": "ECE"},
    {"name": "Roy", "marks": 60, "course": "ECE"},
    {"name": "Tom", "marks": 90, "course": "CSE"},
    {"name": "Tom", "marks": 90, "course": "CSE"}
]

# 1. Find topper
topper = max(students, key=lambda student: student["marks"])
print("Topper:", topper["name"])

# 2. Calculate class average
total = 0

for student in students:
    total = total + student["marks"]

average = total / len(students)

print("Class average:", average)

# 3. Students who scored above 80
print("Students above 80:")

for student in students:
    if student["marks"] > 80:
        print(student["name"])

# 4. Find lowest scorer
lowest = min(students, key=lambda student: student["marks"])

print("Lowest scorer:", lowest["name"])

# 5. Rank students by marks
ranking = sorted(students, key=lambda student: student["marks"], reverse=True)

print("Ranking:")

for student in ranking:
    print(student["name"], student["marks"])

# 6. Find duplicate student records
duplicates = []

for i in range(len(students)):
    for j in range(i + 1, len(students)):
        if students[i] == students[j]:
            if students[i] not in duplicates:
                duplicates.append(students[i])

print("Duplicate records:", duplicates)

# 7. Group students by course
courses = {}

for student in students:
    course = student["course"]

    if course not in courses:
        courses[course] = []

    courses[course].append(student["name"])

print("Students by course:", courses)

# 8. Highest scorer in each course
for course in courses:
    highest = None

    for student in students:
        if student["course"] == course:
            if highest is None or student["marks"] > highest["marks"]:
                highest = student

    print("Highest in", course, ":", highest["name"])

# 9. Final result
print("Final Results:")

for student in students:

    if student["marks"] >= 80:
        result = "Distinction"
    elif student["marks"] >= 40:
        result = "Pass"
    else:
        result = "Fail"

    print(student["name"], ":", result)