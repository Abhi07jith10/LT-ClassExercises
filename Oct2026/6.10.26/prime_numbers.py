#A prime number is a whole number greater than 1 that can only be divided evenly by 1 and itself.

# First few primes: 2, 3, 5, 7, 11, 13, 17, 19, 23, and 29.

num=int(input("enter the number: "))
if num==1:
    print("enter number greater than 1.")
else:
 for i in range(2,num):
    if num%i==0:
        print("num is not prime")
        break
    else:
        print("number is prime")
        break
