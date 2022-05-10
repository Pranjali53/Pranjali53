nums = [0,0,1,1,1,2,2,3,3,4]
New=[]
i=0
while i<len(nums):
    if nums[i] not in New:
        New.append(nums[i])
    i+=1
print(New)
    