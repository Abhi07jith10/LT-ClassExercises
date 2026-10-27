#get the prime factors of a number


#if number=12, the prime factors are 2 and 3, 2x2x3

number=int(input("enter the number:"))

for i in range(1,number):
    if number%i==0:
        for j in range(2,i+1):
            if i%j==0:
                print("")
                break
        else:
            print(j)
#===============================
#sir version
num=int(input("enter the number :"))
while number<=1:
    print("enter a number greater than 1.")
    number=int(input("enter the number: "))

for num in range(1,number+1):
    if number%num==0 and num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)
        