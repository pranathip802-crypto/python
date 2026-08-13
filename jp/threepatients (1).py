class Hospital:
    def __init__(self, patient_name, age, disease, doctor_name):
        self.patient_name = patient_name
        self.age = age
        self.disease = disease
        self.doctor_name = doctor_name


p1 = Hospital("Ravi", 30, "Fever", "Dr. Kumar")
p2 = Hospital("Priya", 25, "Cold", "Dr. Sharma")
p3 = Hospital("Anil", 40, "Diabetes", "Dr. Rao")

for patient in [p1, p2, p3]:
    print(
        patient.patient_name,
        patient.age,
        patient.disease,
        patient.doctor_name
    )