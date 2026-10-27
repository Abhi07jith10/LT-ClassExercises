#check the prime numbers from 100 to 10

for num in range(100,9,-1):
    for i in range(2,num):
        if num%i==0:
            break
    else:
        print(num)


