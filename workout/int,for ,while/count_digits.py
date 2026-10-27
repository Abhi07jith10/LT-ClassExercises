num=int(input("enter the number :"))
temp=num

count=0

while num>0:

    lastdigit=num%10
    if lastdigit>=0:
        count+=1
    num//=10
print(f"the count of the number {temp} is {count}")