

number=int(input("enter the number: "))

while number<=1:
   print("please enter a number greater than 1.")
   number=int(input("enter the number: "))

else:
    for i in range(2,number):
       if number%i==0:
        print(f"the {number} is not a prime number.")
        break

    else:
     print("the number is a prime number.")
