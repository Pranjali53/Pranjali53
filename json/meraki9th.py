import json
py_dict={
    "shopping_list":
        { 
            "chocolate":"15",
            "Biscuits":"50",
            "Diary_milk":"30",
            "ice_cream":"20",
        } 
}
print("Do you want to buy something ::- ")
print("1.Yes or 2.No")
num=int(input("please enter no '1'(For Yes) or '2' (For No) -->>"))
stor=0
if num==1:
    for i in py_dict:
        user1=input("Please tell me what you want ::- ")
        for v in py_dict[i]:
            if user1==v:
                user2=int(input("Please tell me quintity of your item ::- "))
                stor=int(py_dict[i][v])-user2
                break
            else:
                print("Sorry,We do not have item ::-")
            break
        py_dict[i][v]=str(stor)
        json_ob=json.dumps(py_dict,indent=6)
        print(json_ob) 
        break
else:
    print("Ok thanks ,Thank you for visit")
f=open("que_9.json","w")
json.dump(py_dict,f,indent=6)
f.close()