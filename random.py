#wap to remove non prime numebrs from the list

# num=11

# for i in range(2,num):
    # if num%i==0:
        # print("num is not prime number")
    
        # break
# else:
    # print("num is prime number")

nums=[1,2,3,4,8,7,9,11,13,15]   #[3,7,11,13]

for i in nums:
    if i==1:
        nums.remove(i)


for i in nums.copy():           #3
    for j in range(2,i):  #(2,3)  2
        if i%j==0:
            if i in nums:
                nums.remove(i)
            
print(nums)

        



