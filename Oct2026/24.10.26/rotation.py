#rotate the list by 3 times

numbers=[1,2,3,4,5,6,7,8]

#op=[6,7,8,1,2,3,4,5]
for i in range(3):
    element=numbers.pop()
    numbers.insert(0,element)

print(numbers)