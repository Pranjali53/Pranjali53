import json
py_dict={
    "shopping_list":
        { 
            "chaco":"15",
            "Biscuits":"50",
            "Diary_milk":"30",
            "ice_cream":"20",
        } 
}
print("kya ap kharigana chahate hai")
print("1.Yes or 2.Not")
num=int(input("please enter no 1 or 2 -->>"))
stor=0
if num==1:
    for i in py_dict:
        user1=input("enter what you want::")
        for v in py_dict[i]:
            if user1==v:
                user2=int(input("enter how many you want::"))
                stor=int(py_dict[i][v])-user2
                break
            else:
                print("wrong character")
            break
        py_dict[i][v]=str(stor)
        json_ob=json.dumps(py_dict,indent=6)
        print(json_ob) 
        break
else:
    print("Ok thanks ,You can go")
f=open("que_9.json","w")
json.dump(py_dict,f,indent=6)
f.close()