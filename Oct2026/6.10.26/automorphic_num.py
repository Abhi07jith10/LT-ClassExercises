#an integer whose square ends in the exact same digits as the number itself
#Single digits: 0 (0²=0), 1 (1²=1), 5 (5²=25), and 6 (6²=36) 
#Multi-digits: 25 (25²=625), 76 (5776), and 376 (141376).

number=int(input("enter the number: "))
square=number**2
length=len(str(number))

if square% 10**length==number:
    print("The number is an automorphic number.")
else:
    print("The number is not an automorphic number.")

