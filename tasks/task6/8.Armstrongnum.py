#Write a function that accepts a number and checks whether it is an Armstrong number. Then write another
# function that displays all Armstrong numbers from 1 to a given limit.
# Example: For limit 500, display 1, 153, 370, 371, 407.

def armstrong(number):
    total=0
    for i in str(number):
       cube=int(i)**3
       total+=cube

    if total==number:
        print(f"The entered number {number} is an armstrong number.")
    else:
        print(f"The entered number {number} is not an armstrong number.")


armstrong(153)

#=======================================================================================

def armstrong_range(limit):
    for i in range(1,limit+1):
        total=0
        for j in str(i):
            cube=int(j)**3
            total+=cube
        if total==i:
            print(i)

armstrong_range(500)



