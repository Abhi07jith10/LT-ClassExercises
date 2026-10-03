#Write a program to find the sum of all even factors for each number from 10 down to 6. Display the result for each number.

for i in range(10, 5, -1):
    sum = 0

    for j in range(1, i + 1):
        if i % j == 0 and j % 2 == 0:
            sum = sum + j

    print(f"The sum of even factors of {i} is {sum}")




