# Calculate the sum of all elements in a nested list containing 3 rows and 4 columns using nested loops.

numbers = [
 [10, 20, 30, 40],
 [5, 15, 25, 35],
 [2, 4, 6, 8]
]

total=0
for i in numbers:
    for j in i:
        total=total+j

print(total)

    

