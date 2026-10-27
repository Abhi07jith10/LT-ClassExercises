#ip=[1,0,2,3,0,4,0,5,6]
#op=[1,2,3,4,5,6,0,0,0]

nums=[1,0,2,3,0,4,0,5,6]

for i in nums:
    if i==0:
        nums.remove(i)
        nums.append(i)

print(nums)

