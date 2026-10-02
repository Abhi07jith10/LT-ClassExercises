#Count the Digits — Take a number as input and count how many digits it has, using a while loop.

num=int(input("enter the number : "))


total=0
while num>0:
    last_digit=num%10
    total=total+last_digit
    num//=10
print(total)