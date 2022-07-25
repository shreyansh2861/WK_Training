import pymysql.cursors

conn = pymysql.connect(host='localhost',
                       user='root',
                       password='root@1234',
                       database='patient_data',
                       cursorclass=pymysql.cursors.DictCursor)

with conn:
    with conn.cursor() as cursor:
        sql = "select * from patient"
        cursor.execute(sql)
        result = cursor.fetchall()
    print(result)