from abc import ABC, abstractmethod

class Course(ABC):

    def __init__(self, course_name, duration):
        self.course_name = course_name
        self.duration = duration

    @abstractmethod
    def display_course(self):
        pass


class OnlineCourse(Course):

    def display_course(self):
        print("Course Type: Online")
        print("Course Name:", self.course_name)
        print("Duration:", self.duration)


class OfflineCourse(Course):

    def display_course(self):
        print("Course Type: Offline")
        print("Course Name:", self.course_name)
        print("Duration:", self.duration)


online = OnlineCourse("Python Programming", "3 Months")
offline = OfflineCourse("Java Programming", "6 Months")

online.display_course()
print()

offline.display_course()