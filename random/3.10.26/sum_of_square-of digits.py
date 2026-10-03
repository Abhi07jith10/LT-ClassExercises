#Sum of Squares of Digits — 
# Take a number and find the sum of the square of each digit (e.g., 123 → 1² + 2² + 3² = 14).

num=int(input("enter the num"))
temp=num
total=0

while num>0:
    last_d=num%10
    square=last_d**2
    total=total+square
    num//=10

print(f"the sum of square of the digit{temp} is {total}")