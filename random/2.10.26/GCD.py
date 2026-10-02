#GCD of Two Numbers — Given two numbers, find their GCD using a while loop 
# (without using the factor-listing approach — think about the subtraction or remainder method).

num1=int(input("enter the first number: "))
num2=int(input("enter the second number: "))

i=1

while i<=num1:
    if num1%i==0:
        if i==(num2%i):
            print(i)
    i+=1
