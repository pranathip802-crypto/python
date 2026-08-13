class Student:
    college_name = "ABC College"

    def __init__(self, name):
        self.name = name


s1 = Student("Ravi")
s2 = Student("Priya")
s3 = Student("Anil")

print(s1.name, s1.college_name)
print(s2.name, s2.college_name)
print(s3.name, s3.college_name)