class Student:
    def __init__(self, name, age, course, marks):
        self.name = name
        self.age = age
        self.course = course
        self.marks = marks


student = Student("Ravi", 20, "BCA", 85)

print(student.name)
print(student.age)
print(student.course)
print(student.marks)