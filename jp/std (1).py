class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course


s1 = Student("Ravi", 20, "BCA")
s2 = Student("Anil", 21, "B.Tech")
s3 = Student("Priya", 19, "MCA")

print(s1.name, s1.age, s1.course)
print(s2.name, s2.age, s2.course)
print(s3.name, s3.age, s3.course)