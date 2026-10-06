#using for loop



num=int(input("enter the number: "))
total=0
product=1
for i in str(num):
    last_d=num%10
    total=total+int(i)
    product=product*int(i)

if total==product:
    print("Spy nu")
else:
    print("Not spy")