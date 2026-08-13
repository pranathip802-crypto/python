class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}"


class College:
    def get_student_info(self, student):
        return student.get_info()


student = Student("Ravi", 20)
college = College()

print(college.get_student_info(student))