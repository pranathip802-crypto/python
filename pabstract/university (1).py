from abc import ABC, abstractmethod

class UniversityCourse(ABC):

    @abstractmethod
    def study(self):
        pass


class Engineering(UniversityCourse):

    def study(self):
        print("Studying Engineering")


class Medical(UniversityCourse):

    def study(self):
        print("Studying Medical")


class Management(UniversityCourse):

    def study(self):
        print("Studying Management")


courses = [Engineering(), Medical(), Management()]

for course in courses:
    course.study()