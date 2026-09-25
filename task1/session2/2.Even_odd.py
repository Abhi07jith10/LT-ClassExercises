#Even or Odd
#Write a Python program that accepts an integer from the user. If the number is divisible by 2, display that
#it is even. Otherwise, display that it is odd.

number=float(input("Enter the number :"))

if number%2==0:
    print(f"The number {number} is even")
else:
    print(f"The number {number} is odd")