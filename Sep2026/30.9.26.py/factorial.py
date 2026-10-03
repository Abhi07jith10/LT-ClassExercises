#wap to generate the factorial of a given num

num=int(input("enter the number: "))

i=1
fact=1
while i<=num:
    fact=fact*i
    i+=1

print(f"the factorial of the given number is {fact}")

#==============================================================

#another way
while (number>0):
     fact*=number
     number-=1