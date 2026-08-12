from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def work(self):
        pass


class Developer(Employee):
    def work(self):
        print("Developer writes and tests code")


class Tester(Employee):
    def work(self):
        print("Tester tests the software")


developer = Developer()
tester = Tester()

developer.work()
tester.work()