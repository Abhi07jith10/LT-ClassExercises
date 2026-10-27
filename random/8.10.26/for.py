number=int(input("enter the number : "))

while number<=1:
    print("please enter a number that is greater than 1.")
    number=int(input("enter the number : "))
else:
    for i in range(2,number):
        for j in range(2,i+1):
            if number%j==0:
             break
        else:
         print(number)
