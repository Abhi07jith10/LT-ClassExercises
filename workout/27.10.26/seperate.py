#Separate odd and even
# Given numbers = [8, 3, 12, 5, 7, 10, 1], produce two lists: one with odds, one with evens.
# Expected: [3, 5, 7, 1] and [8, 12, 10]

numbers = [8, 3, 12, 5, 7, 10, 1]

odd_list=[]
even_list=[]

for i in numbers:
    if i%2==0:
        even_list.append(i)
    else:
        odd_list.append(i)

print(even_list)
print(odd_list)