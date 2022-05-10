import json

filename = '7th.txt'
dict1 = {}
with open(filename) as data: 
    for line in data:        
        key, value = line.strip().split()  
        dict1[key] = value.strip()
new_file = open("Json_file.json", "w")
json.dump(dict1, new_file)
new_file.close()