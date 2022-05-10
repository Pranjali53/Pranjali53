import json
python_obj = {
  "name": "David",
  "class":"I",
  "age": 6  
}
print(type(python_obj))
json_data = json.dumps(python_obj)
print(json_data)
print(type(json_data))