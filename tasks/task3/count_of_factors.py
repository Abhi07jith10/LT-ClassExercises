#Count the Factors
#Write a Python program using a while loop to count how many factors a given number has.

num=int(input("enter the number : "))

i=1
count=0
while i<=num:
    if num%i==0:
        count+=1 
        
    i+=1

print(f"The total count of factors of a given number is {count} ")