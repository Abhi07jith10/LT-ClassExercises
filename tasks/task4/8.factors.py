#Read a number from the user and print all its factors using a for loop

num=int(input("enter the number : "))

print(f"The factors of the number {num} are : ")

for i in range(1, num+1):
    if num%i==0:
        print(i)