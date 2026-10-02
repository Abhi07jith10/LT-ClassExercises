#Largest Digit in a Number — Take a number as input and find the largest digit in it using a while loop.

num = int(input("Enter a number: "))

largest = 0

while num > 0:
    digit = num % 10

    if digit > largest:
        largest = digit

    num = num // 10

print("Largest digit:", largest)