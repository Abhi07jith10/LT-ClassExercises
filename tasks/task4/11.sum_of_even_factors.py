#Read a number from the user and calculate the sum of only its even factors.

num=int(input("enter the number :"))

total=0
for i in range(1,num+1):
    if num%i==0 and i%2==0:
        total=total+i

print(f"The total sum of the even factors of the number {num} is {total}")