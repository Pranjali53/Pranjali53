num=1221
num1=num
revers=0
i=0
while num>0:
    revers=num%10+(revers*10)
    num//=10
    i+=1
if num1==revers:
    print(num1,"pelindrom")
else:
    print(num1,"not pelindrom")