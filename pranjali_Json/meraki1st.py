import json 
json_obj = '{ "Name":"David", "Class":"I", "Age":6 }' 
python_obj = json.loads(json_obj) 
print(python_obj) 
print("Name: ",python_obj["Name"]) 
print("Class: ",python_obj["Class"]) 
print("Age: ",python_obj["Age"])