#Read a number from the user and find how many even factors it has.

num=int(input("enter the number :"))

count=0
for i in range(1,num+1):
    if num%i==0 and i%2==0:
        count+=1

print(f"The total count of the even factors of the number {num} is {count}")