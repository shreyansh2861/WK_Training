# Doctor Clinic (USING SQLite)

import sqlite3

class Patient:
    choice = 0

    def __init__(self, cursor):
        self.db_cursor = cursor

    def patient_menu(self):
        self.choice = int(input("\n1. CREATE PATIENT\n2. DELETE PATIENT\n3. UPDATE PATIENT\n4. DISPLAY PATIENTS\n5. EXIT\nCHOICE - "))
        if self.choice == 1:
            self.create_patient()
        elif self.choice == 2:
            self.delete_patient()
        elif self.choice == 3:
            self.update_patient()
        elif self.choice == 4:
            self.display_data()
        else:
            exit(1)

    def save_data(self):
        print("[+] COMMITING TO FILE....")
        self.db_cursor.commit()

    def display_data(self):
        print("\n")
        data = self.db_cursor.execute("SELECT * FROM Patient_Data")
        for p in data:
            print(f"Patient's Id - {p[0]} --- Patient_ID")
            print(f"Patient's Firstname - {p[1]} --- firstName")
            print(f"Patient's Lastname - {p[2]} --- lastName")
            print(f"Patient's Gender - {p[3]} --- gender")
            print(f"Patient's Age - {p[4]} --- age")
            print("\n\n")

    def create_patient(self):
        print("\n[+] CREATING PATIENT....")

        #Creating Patient Code
        patient_id = input("ENTER PATIENT ID - ")
        firstname = input("ENTER PATIENT's FIRSTNAME - ")
        lastname = input("ENTER PATIENT's LASTNAME - ")
        gender = input("ENTER PATIENT's GENDER - ")
        age = input("ENTER PATIENT's AGE - ")

        self.db_cursor.execute(
            """INSERT INTO Patient_Data (Patient_ID, firstName, lastName, gender, age) VALUES (?, ?, ?, ?, ?)""",
            (patient_id, firstname, lastname, gender, age))
        print("[+] PATIENT SUCCESSFULLY CREATED !")
        self.save_data()
        print("[+] SAVED FILE !\n")

        self.display_data()

    def delete_patient(self):
        print("[-] DELETING PATIENT....")
        self.display_data()
        patient_id = input("ENTER PATIENT ID YOU WANT TO DELETE - ")

        # Deleting Patient
        self.db_cursor.execute(
            """DELETE FROM Patient_Data WHERE Patient_ID = ?""",
            (patient_id))
        print("[+] PATIENT SUCCESSFULLY DELETED !")

        self.save_data()
        print("[+] SAVED FILE !\n")

        self.display_data()

    def update_patient(self):
        print("[+] UPDATING PATIENT....")
        self.display_data()
        patient_id = int(input("ENTER PATIENT ID YOU WANT TO UPDATE - "))
        patient_field = input("ENTER PATIENT INFORMATION FIELD YOU WANT TO UPDATE - ")
        #update_field = input("ENter")
        updated_value = input("ENTER UPDATED VALUE - ")
        self.db_cursor.execute(
            f"""UPDATE Patient_Data SET {patient_field} = ? WHERE Patient_ID = ?""",
            (updated_value, patient_id))
        # if patient_field == 'firstname':
        #     self.db_cursor.execute(
        #         """UPDATE Patient_Data SET Firstname = ? WHERE Patient_ID = ?""",
        #         (updated_value, patient_id))
        # elif patient_field == "lastname":
        #     self.db_cursor.execute(
        #         """UPDATE Patient_Data SET LastName = ? WHERE Patient_ID = ?""",
        #         (updated_value, patient_id))
        # elif patient_field == "age":
        #     self.db_cursor.execute(
        #         """UPDATE Patient_Data SET Age = ? WHERE Patient_ID = ?""",
        #         (updated_value, patient_id))
        print("[+] PATIENT SUCCESSFULLY UPDATED !")

        self.save_data()
        print("[+] SAVED FILE !\n")


# class Appointment:
#     choice = 0
#     def __init__(self, file_handle):
#         self.appointment = json.load(file_handle)
#     def appointment_menu(self):
#         self.choice = int(input("\n1. GET APPOINTMENT\n2. EDIT APPOINTMENT\n3. DELETE APPOINTMENT\nCHOICE - "))
#         if self.choice == 1:
#             self.get_appointment()
#         elif self.choice == 2:
#             self.edit_appointment()
#         elif self.choice == 3:
#             self.delete_appointment()
#
#     def get_appointment(self):
#         print("[+] FETCHING APPOINTMENT....")
#     def edit_appointment(self):
#         print("[+] EDITING APPOINTMENT....")
#     def delete_appointment(self):
#         print("[-] DELETING APPOINTMENT....")

def main_menu():
    choice = int(input(("1. Patient Menu\n2. Appointment Menu\nChoice - ")))
    if choice == 1:
        cursor = sqlite3.connect("C:/Users/hasnain.merchant/SQL databases/pateint_db.db")
        print("[+] CONNECTED TO DATABASE")
        patient1 = Patient(cursor)
        while True:
            patient1.patient_menu()
    # elif choice == 2:
    #     #ap_file_name = input("ENTER APPOINTMENT FILE NAME (.json) - ")
    #     ap_file_name = "patient_data.json"
    #     appointment_data = open(ap_file_name, "r")
    #     appointment1 = Appointment(appointment_data)
    #     appointment1.appointment_menu()

#if __name__ == "__main__":
    #main_menu()