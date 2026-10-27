#Write a Python program to print all Armstrong numbers between 1 and n.
#1³ + 5³ + 3³ = 1 + 125 + 27 = 153.

num=int(input("enter the number:"))

for i in range(1,num):
    total=0
    for j in str(i):
        cube=int(j)**3
        total+=cube
    if total==i:
        print(i)