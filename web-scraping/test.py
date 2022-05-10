# capton room
List=[]
n=int(input())
i=0
while i<=n:
# for a in range (n):
    P=int(input())
    List.append(P)
    i+=1
for i in range (len(List)):
    c=0
    for j in range (len(List)):
        if List[i] == List[j]:
            c+=1
    if c==1:
        print(List[i])    


#leep year
def is_leap(year):
    leap = False
    # Write your logic here
    if year%100!=0:
        return leap
    elif year%4==0 or year%400==0:
        return True