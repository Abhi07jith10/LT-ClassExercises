#find the missing numbers from a list of sequence of numbers.

numbers=[7,3,1,2,6,9,11,10,15]

missing_numbers=[]
for i in range(min(numbers),max(numbers)+1):
    if i not in numbers:
        missing_numbers.append(i)

print(missing_numbers)