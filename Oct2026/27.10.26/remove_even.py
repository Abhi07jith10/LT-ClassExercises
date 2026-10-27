#wap to remove the even numbers from the given list

numbers=[3,5,1,2,4,7,6,11,10,13,20]

for i in numbers.copy():
    if i%2==0:
        numbers.remove(i)

print(numbers)
