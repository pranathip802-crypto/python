class Student:
    college = "ABC College"

    def __init__(self, name):
        self.name = name


s1 = Student("Ravi")
s2 = Student("Priya")

print("Student 1:", s1.name)
print("College:", s1.college)

print("Student 2:", s2.name)
print("College:", s2.college)

# Change instance variable
s1.name = "Anil"

print("Updated name:", s1.name)
print("Other student:", s2.name)

# Class variable is shared
print("Class variable:", Student.college)