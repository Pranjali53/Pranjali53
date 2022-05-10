import json 
json_obj = '{ "Name":5j, "Class":9j, "Age":6j}' 
python_obj = json.loads(json_obj) 
print(python_obj) 