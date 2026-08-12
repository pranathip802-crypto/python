from abc import ABC, abstractmethod

class Person(ABC):

    @abstractmethod
    def role(self):
        pass


class Student(Person):
    def role(self):
        print("Student studies")


class Teacher(Person):
    def role(self):
        print("Teacher teaches students")


student = Student()
teacher = Teacher()

student.role()
teacher.role()