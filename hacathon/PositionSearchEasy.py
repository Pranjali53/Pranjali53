nums = [-1,0,3,5,9,12] 
target =int(input("enter any targt : "))
i=0
while i<len(nums):
    if target in nums:
        pass
    else:
        print(nums[0])
    i+=1
print(nums.index(target))   