class Student:
    def __init__(self, marks):
        self.marks = marks

    def total(self):
        return sum(self.marks)

    def average(self):
        return self.total() / len(self.marks)


student = Student([80, 90, 85, 75, 95])

print("Total:", student.total())
print("Average:", student.average())