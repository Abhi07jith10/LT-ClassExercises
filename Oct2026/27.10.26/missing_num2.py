
numbers=[13, 25, 1, 21, 9, 5] #17
numbers.sort()
step=numbers[1]-numbers[0]
print(step)

for i in range(min(numbers),max(numbers),step):
    if i not in numbers:
        numbers.append(i)

numbers.sort()
print(numbers)
