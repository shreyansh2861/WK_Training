from functools import reduce


patient_dobs = ['21-02-1981','03-02-2006','12-01-1950']

"""def get_yob(patient_dobs):
    patient_yobs=[]
    for dob in patient_dobs:
        patient_yobs.append(int(dob.split('-')[2]))
    return patient_yobs


def get_ages(patient_yobs):
    patient_ages=[]
    current_year = 2022
    for age in patient_yobs:
        patient_ages.append(current_year-age)
    return patient_ages

def get_status(get_yob,get_ages,dobs):
    is_major = []
    ages = get_ages(get_yob(dobs))
    for age in ages:
        if age>=18:
            is_major.append(age)
    return is_major


print(get_status(get_yob,get_ages,patient_dobs))
"""


# Using Functional Programming

def get_yob(dob):
    return dob.split('-')[2]

patient_yobs = list(map(get_yob,patient_dobs))

def get_ages(yob):
    return 2022-int(yob)

patient_ages = list(map(get_ages,patient_yobs))

def is_major(age):
    if age>=18:
        return age

major = list(filter(is_major,patient_ages))

print(major)


"""Lambda/nameless/anonymous functions
similar to is_major function
lambda age: age>=18

simply used returns true and false

using direct:
major = list(filter(lambda age: age>=18,patient_ages))

"""

#find avg patient age

def add(age1,age2):
    return age1+age2

age_total = reduce(add, patient_ages)#can also use lambda functions

print(age_total/len(patient_ages))