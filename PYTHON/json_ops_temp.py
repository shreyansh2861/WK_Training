import json

def load_data():
    with open("resources/patient_data.json", 'r') as file_handle:
        json_data = json.load(file_handle)
        return json_data
patient_data = load_data()

def main_menu():
    a = True
    while True:
        print("Select From the following : \n 1. Patient Section \n 2. Appointment Section \n 3. Exit")

        choice = int(input())

        if choice == 1:
            patient_section()
        elif choice == 3:
            exit()



def patient_section():
    print("Select from the following : \n 1. Update Patient Data \n 2. Delete Patient Data \n 3. Add Patient \n 4. "
          "Display All Patient Data \n 5. Go To Main Page")

    choice = int(input())

    if choice == 1:
        print("Enter Patient Id : ")
        id = int(input())
        print("Enter Updated First Name : ")
        name = str(input())
        update_data(id, name, patient_data)
    elif choice == 2:
        delete_data()
    elif choice == 3:
        add_patient()
    elif choice == 4:
        display_data()
    elif choice == 5:
        main_menu()


def append_data(x):
    with open("resources/patient_data.json", 'a') as file_handle:
        file_handle.write(",")
        file_handle.write(json.dumps(x))
        file_handle.close()


def add_patient():
    print("patient_id : ")
    patient_id = int(input())
    print("First Name : ")
    firstName = str(input())
    print("Last Name : ")
    lastName = str(input())

    print("Gender : ")
    gender = str(input())

    print("Age : ")
    age = int(input())

    print("Enter Address : ")
    print("Street : ")
    street = str(input())
    print("City : ")
    city = str(input())
    print("State : ")
    state = str(input())

    print("Phone number : ")
    phno = int(input())
    print("Phone Type : ")
    type = str(input())

    x = {
        "patient_id": patient_id,
        "firstName": firstName,
        "lastName": lastName,
        "gender": gender,
        "age": age,
        "address": {
            "street": street,
            "city": city,
            "state": state
        },
        "phoneNumbers": [
            {
                "type": type,
                "number": phno
            }
        ]
    }

    patient_data["patient_list"].append(x)

    save_data(patient_data)



def delete_data():
    print("Enter Id to be deleted : ")
    choice = int(input())
    pd = {"patient_list": []}
    for i in patient_data["patient_list"]:
        if i["patient_id"] != choice:
            pd["patient_list"].append(i);

    with open("resources/patient_data.json", 'w') as file_handle:
        json.dump(pd,file_handle);
    load_data()




def display_data():
    for i in patient_data["patient_list"]:
        print("----------------------------------------------------")
        print("Patient Id : ", i["patient_id"])
        print("Patient Name : ", i["firstName"], "\t", i["lastName"])
        print("Gender : ", i["gender"])
        print("Age : ", i["age"])
        print("Address : ", i["address"]["street"], ", ", i["address"]["city"], ", ", i["address"]["state"])
        print("Phone Number : ", i["phoneNumbers"][0]["number"], "\tType : ", i["phoneNumbers"][0]["type"])
        print("----------------------------------------------------")
        print("\n")



def update_data(id, name, pdata):
    for patient in pdata["patient_list"]:
        if patient["patient_id"] == id:
            patient["firstName"] = name
    save_data(patient_data)


def save_data(pdata):
    with open("resources/patient_data.json", 'w') as filehandle:
        json.dump(pdata, filehandle, indent=4)


main_menu()

patient_data = load_data()
"""

print(patient_data)

update_data(1, "Meowth", patient_data)
print(patient_data)
"""

# print(patient_data["patient_list"])
