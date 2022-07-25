import sqlite3


def initialize_conn():
    try:
        con = sqlite3.connect(r"patient_data.db")
        return con
    except Exception as e:
        print(e)


def get_data(con):
    cursor = con.execute("select * from patient")
    for row in cursor:
        print(row)


def update_patient(con, pid, age):
    con.execute(f"update patient set pAge={age} where pID={pid}")
    con.commit()
    # print(cursor)


def delete_patient(con, pid):
    del_status = 'Active'
    con.execute(f"update patient set pStatus='{del_status}' where pID={pid}")
    con.commit()


connection = initialize_conn()
get_data(connection)
update_patient(connection, 2, 23)
get_data(connection)
delete_patient(connection, 1)
get_data(connection)
