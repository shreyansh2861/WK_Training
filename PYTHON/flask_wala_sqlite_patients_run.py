from flask import Flask, render_template, request
import sqlite3 as sql

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/enternew')
def new_patient():
    return render_template('new_patient.html')


@app.route('/addrec', methods=['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        try:
            id = request.form['patientID']
            fnm = request.form['firstName']
            lnm = request.form['lastName']
            gen = request.form['gender']
            age = request.form['age']
            mob = request.form['phNO']

            with sql.connect("patients1.db") as con:
                cur = con.cursor()
                cur.execute(
                    "INSERT INTO patients (patientID,firstName,lastName,gender,age,phNO)VALUES(?, ?, ?, ?, ?, ?)",
                    (id, fnm, lnm, gen, age, mob))

                con.commit()
                msg = "Record successfully added"
        except:
            con.rollback()
            msg = "error in insert operation"

        finally:
            return render_template("result.html", msg=msg)
            con.close()


@app.route('/list')
def list():
    con = sql.connect("patients1.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from patients")

    rows = cur.fetchall()
    return render_template("list.html", rows=rows)


if __name__ == '__main__':
    app.run(debug=True)
