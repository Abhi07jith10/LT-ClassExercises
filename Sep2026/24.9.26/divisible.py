num=int(input("enter the no: "))

if num%3==0 and num%5==0:
    print("The number is divisible by both 3 and 5")
elif num%3==0 or num%5==0:
    print("The number is either divisble by both 3 or 5")
else:
    print("The number is not divisible by both 3 and 5")
