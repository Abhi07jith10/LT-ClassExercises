#Sum of Even Factors
#Write a Python program using a while loop to find the sum of all even factors of a given number.

#10...1,2,5,10

num=int(input("enter the number : "))

i=1
total=0

while i<=num: 
    if num%i==0 and i%2==0:
        total=total+i
    i=i+1
print(f"the total of the even factors of the given number is {total}")

    
