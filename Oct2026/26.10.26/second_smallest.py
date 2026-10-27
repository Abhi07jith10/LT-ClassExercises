#wap to get the second smallest num from the list

num=[1,5,2,7,10,2,9]

smallest=num[0]

second_smallest=num[0]

for i in num:
    if i <smallest:
        second_smallest=smallest
        smallest=i
    elif i <second_smallest and i >smallest:
        second_smallest=i
print(second_smallest)