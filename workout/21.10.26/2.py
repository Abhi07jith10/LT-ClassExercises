# Write a program to display all Armstrong numbers
#  from n down to 1

num=int(input("enter the number: "))

for i in range(num,0,-1):
    total=0
    for j in str(i):
        cube=int(j)**3
        total+=cube
    if total==i:
        print(i)