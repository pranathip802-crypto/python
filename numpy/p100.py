import numpy as np

# Student marks
marks = np.array([
    [85, 90, 80],
    [70, 65, 75],
    [95, 92, 96],
    [50, 55, 60],
    [40, 45, 35]
])

students = np.array([
    "Joy",
    "Asha",
    "lilly",
    "Sai",
    "Esha"
])

# 1. Total marks of each student
total = np.sum(marks, axis=1)

# 2. Average marks of each student
average = np.mean(marks, axis=1)

# 3. Highest scorer
highest_index = np.argmax(total)

# 4. Lowest scorer
lowest_index = np.argmin(total)

# 5. Subject-wise average
subject_average = np.mean(marks, axis=0)

# 6. Pass/Fail count
pass_students = np.sum(average >= 50)
fail_students = np.sum(average < 50)

# 7. Grades
grades = np.where(
    average >= 90, "A",
    np.where(
        average >= 75, "B",
        np.where(
            average >= 60, "C",
            np.where(average >= 50, "D", "F")
        )
    )
)

# 8. Rank
rank = np.argsort(np.argsort(-total)) + 1

# 9. Class average
class_average = np.mean(average)

# 10. Students above class average
above_average = students[average > class_average]


print("----- STUDENT MARKS ANALYZER -----")

print("\nTotal Marks:")
for i in range(len(students)):
    print(students[i], ":", total[i])

print("\nAverage Marks:")
for i in range(len(students)):
    print(students[i], ":", average[i])

print("\nHighest Scorer:")
print(students[highest_index], ":", total[highest_index])

print("\nLowest Scorer:")
print(students[lowest_index], ":", total[lowest_index])

print("\nSubject-wise Average:")
print(subject_average)

print("\nPass Students:", pass_students)
print("Fail Students:", fail_students)

print("\nGrades:")
for i in range(len(students)):
    print(students[i], ":", grades[i])

print("\nRank:")
for i in range(len(students)):
    print(students[i], ":", rank[i])

print("\nClass Average:", class_average)

print("\nStudents Above Class Average:")
print(above_average)