#A neon number is a number where the sum of the digits of its square is equal to the original number.

# Example

#  Number: 9
#  Square: 9 × 9 = 81
#  Sum of digits of square: 8 + 1 = 9
#  Result: Because the sum equals the original number, 9 is a neon number

num=int(input("enter the number: "))
square=num**2
total=0
for i in str(square): #81
    total=total+int(i)

if total==num:
    print(f"the number {num} is a neon number.")
else:
    print(f"the number {num} is not a neon number.")

