from abc import ABC, abstractmethod

class Course(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def start(self):
        pass

    def display_course_details(self):
        print("Course:", self.name)


class PythonCourse(Course):

    def start(self):
        print("Python course started")


course = PythonCourse("Python Programming")

course.start()
course.display_course_details()