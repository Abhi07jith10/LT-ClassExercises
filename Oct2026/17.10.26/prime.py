def is_prime(num1):
    for i in range(2,num1):
        if num1%i==0:
            print("Not prime")
            break
    else:
        print("prime num")

is_prime(7)