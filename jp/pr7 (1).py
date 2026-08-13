class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject


class Course:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display(self):
        print("Course:", self.name)

        for student in self.students:
            print(student.name)


students = []
teachers = []
courses = []


students.append(Student("Ravi", 20))
students.append(Student("Priya", 21))

teachers.append(Teacher("Mr. Kumar", "Python"))
teachers.append(Teacher("Mrs. Sharma", "Maths"))

python_course = Course("Python")

python_course.add_student(students[0])
python_course.add_student(students[1])

courses.append(python_course)

print("Students:")

for student in students:
    print(student.name, student.age)

print("\nTeachers:")

for teacher in teachers:
    print(teacher.name, teacher.subject)

print("\nCourses:")

for course in courses:
    course.display()