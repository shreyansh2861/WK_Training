import json

with open("resources\\patient_data.json", 'r') as file_handle:
    json_data = json.load(file_handle)
    #return json_data

print(json_data)