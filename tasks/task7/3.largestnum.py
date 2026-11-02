# Find the largest number in a nested list without using the max() function.

numbers = [
 [12, 45, 23],
 [67, 34, 89],
 [10, 56, 78]
]

largest=0
for i in numbers:
    if max(i)>largest:
        largest=max(i)


print(f"the largest number is {largest}")