def is_prime(num1):
    for i in range(2,num1):
        if num1%i==0:
            print("Not prime")
            break
    else:
        print("prime num")



for i in range(5):
    num=int(input("enter the number: "))
    while num<=1:
        num=int(input("enter the number: "))
        
    is_prime(num)