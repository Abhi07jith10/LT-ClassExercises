#Read a number from the user and find the total number of factors it has.

num=int(input("enter the number : "))

count=0
for i in range(1,num+1):
    if num%i==0:
        count+=1
print(f"The total count of factors for the number {num} is {count}")