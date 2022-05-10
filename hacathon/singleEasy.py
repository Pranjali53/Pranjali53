nums = [2,2,1,3,3,4]
new=[]
for i in range(len(nums)):
    c=0
    for j in range(len(nums)):
        if nums[i]==nums[j]:
            c+=1
    if c==1:
        new.append(nums[i])
print(new)