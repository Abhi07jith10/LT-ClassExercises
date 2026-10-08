#ternary operators
num=int(input("enter the number"))
print(f"the number {num} is divisible" if num%3==0 and num%5==0 else f"number {num} is not divisible" )