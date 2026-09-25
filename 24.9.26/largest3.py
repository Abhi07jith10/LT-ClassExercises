#get the largst num among thre three nos given by user

num1=int(input("enter the no: "))
num2=int(input("enter the no: "))
num3=int(input("enter the no: "))


if num1>num2:
    if num1>num3:
        print("Num1 is the largest")
    else:
        print("Num3 is the largest")
elif num2>num3:
    print("Num2 is the largest")
else:
    print("Num 3 is the largest")

