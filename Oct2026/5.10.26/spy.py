#spy number is the no in which 
#the sum of digits of number equal to the product of digits in a number.
#ex: 1 + 1 + 2 + 4 = 8 and 1 × 1 × 2 × 4 =8

num=int(input("enter the number:"))

product=1
total=0

while num>0:
    last_d=num%10
    total=total+last_d
    product=product*last_d
    num//=10 

if total==product:
    print("The number is a spy number")
else:
    print("Not spy num")

#===============================================
    
    