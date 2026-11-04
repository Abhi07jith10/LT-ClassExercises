#Remove duplicates, keep order
# Given numbers = [4, 2, 4, 7, 2, 9, 7, 1], remove duplicates without changing the original order.
# Expected: [4, 2, 7, 9, 1]

numbers = [4, 2, 4, 7, 2, 9, 7, 1]

for i in numbers.copy():
    count=numbers.count(i)
    if count>1:
        numbers.remove(i)

numbers.sort()
print(numbers)
