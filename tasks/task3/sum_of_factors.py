#Sum of Factors
# Write a Python program using a while loop to calculate the sum of all factors of a given number.

num=int(input("enter the number : "))

i=1
total=0

while i <=num:
    if num%i==0:
        total=total+i
    i+=1
print(total)