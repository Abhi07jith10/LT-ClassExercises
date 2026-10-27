#wap to print the largest among the numbers

number=[3,2,4,6,10,11,2,3,5]

largest_num=0
for i in number:
    if i>largest_num:
        largest_num=i
    
print(largest_num)