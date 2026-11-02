# Count the total number of even numbers present in a nested list.

numbers = [
 [12, 15, 18],
 [21, 24, 27],
 [30, 33, 36]
]

count=0
for i in numbers:
    for j in i:
        if j%2==0:
            count+=1

print(f"total even numbers is {count}")
