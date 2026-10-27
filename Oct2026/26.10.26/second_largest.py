#wap to get the second largest num from the list

num=[1,5,2,7,10,2,9]

largest=0
second_largest=0

for i in num:
    if i >largest:
        second_largest=largest
        largest=i
    elif i>second_largest and i<largest:
        second_largest=i

print(second_largest)