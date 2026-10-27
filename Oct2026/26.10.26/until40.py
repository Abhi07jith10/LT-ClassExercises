#create a list and asks user to enter the value and add it to the list until the user enters 40

number=[]

while True:
    num=int(input("enter the number:"))

    if num==40:
        number.append(num)
        print(number)
        break