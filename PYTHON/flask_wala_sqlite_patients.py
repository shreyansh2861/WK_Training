import sqlite3

conn = sqlite3.connect('patients1.db')
print("Opened database successfully")
c = conn.cursor()

c.execute('''CREATE TABLE patients(patientID INT, firstName TEXT, lastName TEXT, gender TEXT, age INT, phNO INT)''')
print("Table created successfully")
conn.close()