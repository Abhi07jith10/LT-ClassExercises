#Write a program to find the sum of all even numbers between 1 and 100.

total=0
for i in range(1,101):
    if i%2==0:
        total=total+i

print(total)