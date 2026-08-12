from abc import ABC, abstractmethod

class Course(ABC):

    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    @abstractmethod
    def start(self):
        pass


class ProgrammingCourse(Course):

    def start(self):
        print(self.name, "started")


class DesignCourse(Course):

    def start(self):
        print(self.name, "started")


class BusinessCourse(Course):

    def start(self):
        print(self.name, "started")


courses = [
    ProgrammingCourse("Python", "3 Months"),
    DesignCourse("Graphic Design", "4 Months"),
    BusinessCourse("Business Management", "6 Months")
]

for course in courses:
    course.start()