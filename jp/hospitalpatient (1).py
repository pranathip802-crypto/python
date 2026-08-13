class HospitalPatient:
    def __init__(self, name, age, disease, doctor):
        self.name = name
        self.age = age
        self.disease = disease
        self.doctor = doctor

    def display(self):
        print("Patient:", self.name)
        print("Age:", self.age)
        print("Disease:", self.disease)
        print("Doctor:", self.doctor)


patient = HospitalPatient(
    "Ravi",
    30,
    "Fever",
    "Dr. Kumar"
)

patient.display()