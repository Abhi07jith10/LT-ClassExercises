"""
A perfect number is a positive whole number that equals the sum of 
its proper positive divisors, excluding the number itself
6 >> 1,2,3
8 >> 1,2,4
eg:
6: Proper divisors are 1, 2, and 3. Their sum (1 + 2 + 3) equals 6.
28: Proper divisors are 1, 2, 4, 7, and 14. Their sum equals 28.
# 8: proper divisors  1,2,4


wap to check the given the number is perfect or not
"""

num=int(input("enter the number: "))

i=1
total=0
while i<num:
    if num%i==0:

        total+=i
    i+=1

if total==num:
    print(f"The given number {num} is a perfect number.")
else:
    print(f"The given number {num} is not a perfect number.")


