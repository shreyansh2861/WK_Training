import json


def get_patient_iterator():
    with open(f'C:/Users/shreyansh.patil/OneDrive - Wolters Kluwer/Desktop/Playwright demo/PYTHON/resources/patient_data.json') as json_file:
        json_data = json.load(json_file)
        return iter(json_data["patient_list"])

def print_patients(p_itr):
    while True:
        try:
            print(next(p_itr))
        except StopIteration:
            break


print_patients(get_patient_iterator())