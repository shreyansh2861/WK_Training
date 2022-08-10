from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import db_operations as db

app = Flask(__name__)
CORS(app)



@app.route('/', methods=['GET'])
def get_handler():
    print("Inside get handler")
    cursor = db.initialize_connection()
    patient_data = db.get_patient_data(cursor)
    header = ('PatientID', 'Firstnname', 'Lastname', 'Gender', 'Age')
    response = jsonify(message=patient_data, header=header)
    return response


@app.route('/', methods=['POST'])
# @cross_origin()
def post_handler():
    print("Inside Post Handler")
    req_data = request.get_json()
    id = write_to_db(req_data)
    return f'<center><h4>Patient Number {id} Added Successfully</h5></center>'

def write_to_db(req_data):
    cursor = db.initialize_connection()
    print(req_data)
    patient_id, firstname, lastname, gender, age = req_data.values()
    db.add_patient_to_db(cursor, patient_id, firstname, lastname, gender, age)
    return patient_id

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, threaded=True, debug=True)