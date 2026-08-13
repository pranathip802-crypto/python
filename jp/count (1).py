class Student:
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1


s1 = Student("Ravi")
s2 = Student("Priya")
s3 = Student("Anil")

print("Total objects:", Student.count)