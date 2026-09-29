#Sum of Odd Factors
#Write a Python program using a while loop to find the sum of all odd factors of a given number.

num=int(input("enter the number : "))

i=1
total=0

while i<=num:
    if num%i==0 and i%2!=0:
        total+=i
    i+=1
print(f"The total sum of the odd factors of the given number is {total}")
