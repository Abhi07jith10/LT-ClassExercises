#wap to get the factors of a number enter by user

#8    1,2,4,8
#10   1,2,5,10
#15   1,3,5,15

num=int(input("enter the number :"))
i=1

while i<=num:
    if num%i==0:   #not i%num . vvimp  
        print(i)
    i+=1
