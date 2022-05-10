import json
python_obj = {
    '4': 5, 
    '6': 7, 
    '1': 3, 
    '2': 4}
print(type(python_obj))
json_data = json.dumps(python_obj)
print(json_data)
print(type(json_data))