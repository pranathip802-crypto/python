class Teacher:
    def __init__(self, name, subject, experience):
        self.name = name
        self.subject = subject
        self.experience = experience


teachers = [
    Teacher("Ravi", "Python", 5),
    Teacher("Priya", "Java", 7),
    Teacher("Anil", "Maths", 10)
]

for teacher in teachers:
    print(teacher.name, teacher.subject, teacher.experience)