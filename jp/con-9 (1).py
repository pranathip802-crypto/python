class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.students = []

    def enroll(self, student):
        self.students.append(student)

    def display_students(self):
        print("Course:", self.course_name)
        print("Students:")

        for student in self.students:
            print(student)


course = Course("Python")

course.enroll("Ravi")
course.enroll("Priya")
course.enroll("Anil")

course.display_students()