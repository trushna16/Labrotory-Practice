class ExpertSystem:
    def __init__(self):
        self.symptoms = []
        self.diseases = []

    def add_symptom(self, symptom):
        self.symptoms.append(symptom)

    def add_disease(self, disease, symptom_list):
        self.diseases.append((disease, symptom_list))

    def get_matching_diseases(self, user_symptoms):
        matching_diseases = []

        for disease, symptom_list in self.diseases:
            if set(symptom_list).issubset(user_symptoms):
                matching_diseases.append(disease)

        return matching_diseases


# Create an instance of the ExpertSystem
expert_system = ExpertSystem()

# Add symptoms
expert_system.add_symptom("Fever")
expert_system.add_symptom("Cough")
expert_system.add_symptom("Headache")
expert_system.add_symptom("Nausea")

# Add diseases and associated symptoms
expert_system.add_disease("Common Cold", ["Cough"])
expert_system.add_disease("Flu", ["Fever", "Cough", "Headache"])
expert_system.add_disease("Migraine", ["Headache", "Nausea"])
expert_system.add_disease("COVID-19", ["Fever", "Cough", "Headache", "Nausea"])

# Get user input for symptoms
user_symptoms = []
num_symptoms = int(input("Enter the number of symptoms you are experiencing: "))
for _ in range(num_symptoms):
    symptom = input("Enter a symptom: ")
    user_symptoms.append(symptom)

# Get matching diseases based on user symptoms
matching_diseases = expert_system.get_matching_diseases(user_symptoms)

# Display the matching diseases
if matching_diseases:
    print("Possible diseases based on your symptoms:")
    for disease in matching_diseases:
        print("- " + disease)
else:
    print("No matching diseases found based on your symptoms.")
