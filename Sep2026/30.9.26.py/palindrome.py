#wap to reverse a number enter by user

num=int(input("enter the number : "))

reversed=0
while num>0:
    last_digit=num%10
    reversed=reversed*10 + last_digit # 0*10+3=3, 3*10+2=32, 32*10+1=321
    num//=10

print(f"The reversed digit is {reversed}")