class Course:
    institute_name = "ABC Institute"

    def __init__(self, course_name, duration):
        self.course_name = course_name
        self.duration = duration


c1 = Course("Python", "3 Months")
c2 = Course("Java", "4 Months")

print(c1.institute_name, c1.course_name, c1.duration)
print(c2.institute_name, c2.course_name, c2.duration)