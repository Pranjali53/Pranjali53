import json
a=["neelam","programer",24,2400]
b=["komal","trainer",24,20000]
c=["anuradha","HR",25,40000]
d=["abhishek","manager",29,63000]
e=[a,b,c,d]
list=["name","designation","age","salary"]
f=["emp1","emp2","emp3","emp4"]
w={}
i=0
while i<len(e):
    j=0
    s={}
    while j<len(e[i]):
        if j==0:
            s[list[j]]=e[i][j]
        if j==1:
            s[list[j]]=e[i][j]
        if j==2:
            s[list[j]]=e[i][j]
        if j==3:
            s[list[j]]=e[i][j]
        j=j+1
    w[f[i]]=s
    i=i+1
print(w)
with open("meraki8.json","w")as dic1:
    json.dump(w,dic1,indent=4)