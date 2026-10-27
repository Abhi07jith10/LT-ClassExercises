#wap to remove non pimre numebrs from the list

nums=[1,3,2,4,8,7,9,11,13,15]

new=[]
for i in nums:
    for j in range(2,i+1):
        if i%j==0:
            print(i)


            

