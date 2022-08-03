import csv
from posixpath import split

def get_emp_data():
    with open('PYTHON\employee_data.csv','r') as emp_file:
        emp_data = csv.DictReader(emp_file)
        for emp in emp_data:
            yield emp

for i in get_emp_data():
    print(i)

def process_pension(func):
    for item in func():
        print(f'Dear {item["first_name"]}, your pension will soon be credited')


def age(birthdate):
    return 22 - int(birthdate.split('-')[2])

@process_pension
def get_pensioners():
    #pemp = {}
    for emp in get_emp_data():
        if age(emp["birth_date"]) >= 60:
            #pemp["first_name"] = emp["first_name"]
            #yield pemp
            yield emp


process_pension(get_pensioners())