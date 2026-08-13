class Student:
    school_name = "ABC School"

    def __init__(self, name):
        self.name = name


s1 = Student("Ravi")
s2 = Student("Priya")

print(s1.name, s1.school_name)
print(s2.name, s2.school_name)