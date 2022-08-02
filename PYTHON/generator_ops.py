import json

def patient_generator():
    with open(f'C:/Users/shreyansh.patil/OneDrive - Wolters Kluwer/Desktop/Playwright demo/PYTHON/resources/patient_data.json') as json_file:
        json_data = json.load(json_file)
        for patient in json_data["patient_list"]:
            yield patient


print(patient_generator())
print(next(patient_generator()))
print(next(patient_generator()))

#for i in patient_generator():
#    print(i)