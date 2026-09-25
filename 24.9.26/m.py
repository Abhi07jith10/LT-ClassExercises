#wap to findd the largest no among 3 nos using AND operator

num1=int(input("enter the no: "))
num2=int(input("enter the no: "))
num3=int(input("enter the no: "))


if num1> num2 and num3:
    print("num1 is largest")

elif num2>num1 and num3:
    print("num2 is largest")

else:
    print("num3 is largest")

