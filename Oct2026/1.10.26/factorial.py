#wap to generate the factorial of numbers from 3 to 5

for i in range(3,6):
    fact=1
    for j in range(1,i+1):
        fact=fact*j

    print(f"the factorial of the number {i} is {fact}")

