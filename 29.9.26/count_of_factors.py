#wap to get the count of factors of a number given

number=int(input("enter the number : "))
i=1
count=0

while (i<=number):
    if number%i==0:
        count+=1
    i+=1

print(f"The total number of factors are {count}")