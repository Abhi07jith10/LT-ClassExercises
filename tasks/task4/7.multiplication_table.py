#Read a number from the user and print its multiplication table from 1 to 10.

num=int(input("enter the number: "))

print(f"The multiplication table for the number {num} is given below")

for i in range(1,11):
    mul=i*num
   
    print(f"{i} x {num} = {mul} ")