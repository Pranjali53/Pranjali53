nums = [5,7,7,8,8,10]
target=8
L=[]
L2=[-1,-1]
i=0
while i<len(nums):
    if target==nums[i]:
        L.append(i)
    i+=1
if target not in nums:
    print(L2)
print(L)
   