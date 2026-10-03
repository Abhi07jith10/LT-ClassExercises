#Write a program to find and display the factorial of each number from 6 down to 1.
# Example order: 6!, 5!, 4!, 3!, 2!, 1!.

for i in range(6,0,-1):
    fact=1
    for j in range(1,i+1):
        fact=fact*j

    print(f"the factorial of the number {i} is {fact}")
    
