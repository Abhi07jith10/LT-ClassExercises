#Find the Factors
#Write a Python program using a while loop to find and display all the factors of a given number.

#8 .... 1,2,4,8
#10.... 1,2,5,10
#25.... 1,5,25

num=int(input("enter the number : ")) #10

i=1

while i<=num:
    if num%i==0:
        print(i)
    i+=1
