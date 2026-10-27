

num=int(input("enter the number : "))


total=0
while num>0:
    last_digit=num%10
    total+=last_digit
    num//=10
print(total)

