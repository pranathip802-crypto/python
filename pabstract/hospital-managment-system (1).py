from abc import ABC, abstractmethod

class HospitalEmployee(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def work(self):
        pass


class Doctor(HospitalEmployee):

    def work(self):
        print(self.name, "treats patients")


class Nurse(HospitalEmployee):

    def work(self):
        print(self.name, "takes care of patients")


class Pharmacist(HospitalEmployee):

    def work(self):
        print(self.name, "provides medicines")


employees = [
    Doctor("Dr. Rahul"),
    Nurse("Anita"),
    Pharmacist("Raj")
]

for employee in employees:
    employee.work()