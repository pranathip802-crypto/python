from abc import ABC, abstractmethod

class Course(ABC):

    @abstractmethod
    def start_course(self):
        pass

    @abstractmethod
    def get_duration(self):
        pass


class OnlineCourse(Course):

    def start_course(self):
        print("Online course started")

    def get_duration(self):
        print("Online Course Duration = 3 months")


class OfflineCourse(Course):

    def start_course(self):
        print("Offline course started")

    def get_duration(self):
        print("Offline Course Duration = 6 months")


online = OnlineCourse()
offline = OfflineCourse()

online.start_course()
online.get_duration()

offline.start_course()
offline.get_duration()