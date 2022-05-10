number = [2,7,11,15]
num = 9
total_sum=[]
i=0
while i<len(number):
    j=0
    while j<len(number):
        if number[i]+number[j]==num:
            total_sum.append(i)
            total_sum.append(j)
        j+=1
    i+=1
new=[]
i=0
while i<len(total_sum):
    if total_sum[i] not in new:
        new.append(total_sum[i])
    i+=1
print(new)