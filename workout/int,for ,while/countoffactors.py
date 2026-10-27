#count the factors of given number

num=int(input("enter the number:"))
i=1
count=0

while i<=num:
    if num%i==0:
        count+=1
        print(i)
    
    i+=1
print(f"the total count is {count}")



