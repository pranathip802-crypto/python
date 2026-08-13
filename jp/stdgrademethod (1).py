class Student:
    def grade(self, marks):
        if marks >= 90:
            return "A"
        elif marks >= 80:
            return "B"
        elif marks >= 70:
            return "C"
        elif marks >= 60:
            return "D"
        else:
            return "F"


student = Student()

print(student.grade(85))