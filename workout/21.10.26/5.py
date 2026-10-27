#Write a program to display all
#  three-digit Armstrong numbers using loops


for i in range(100,1000,1):
    total=0
    for j in str(i):
        cube=int(j)**3
        total+=cube
    if total==i:
        print(i)    