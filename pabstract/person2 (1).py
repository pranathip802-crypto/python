from abc import ABC, abstractmethod

class Person(ABC):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def display_role(self):
        pass


class Student(Person):

    def display_role(self):
        print("Role: Student")
        print("Name:", self.name)
        print("Age:", self.age)


class Teacher(Person):

    def display_role(self):
        print("Role: Teacher")
        print("Name:", self.name)
        print("Age:", self.age)


class Doctor(Person):

    def display_role(self):
        print("Role: Doctor")
        print("Name:", self.name)
        print("Age:", self.age)


student = Student("Rahul", 20)
teacher = Teacher("Anita", 35)
doctor = Doctor("Raj", 40)

student.display_role()
print()

teacher.display_role()
print()

doctor.display_role()