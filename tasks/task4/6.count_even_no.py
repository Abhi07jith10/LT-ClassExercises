#Write a program to count how many even numbers are present between 1 and 100.

count=0
for i in range(1,101):
    if i%2==0:
        count+=1
print(count)