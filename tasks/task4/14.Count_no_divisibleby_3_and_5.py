#Read a number n from the user and find the total count of numbers from 1 to n that are divisible by both 3 and 5.

n=int(input("enter the number : "))

count=0
for i in range(1,n+1):
    if i%3==0 and i%5==0:
        
        count+=1

print(f"the total count of numbers that are divisible by both 3 and 5 are {count}")