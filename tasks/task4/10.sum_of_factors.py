#Read a number from the user and calculate the sum of all its factors.

num=int(input("enter the inpur: "))

total=0
for i in range(1,num+1):
    if num%i==0:
        total=total+i

print(total)