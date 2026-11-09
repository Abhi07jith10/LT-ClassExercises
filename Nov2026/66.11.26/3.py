#wap to return the even numbers from numbers 1 to 20 in a list
#return the list of square of numbers from even list above.
#from the final squared lsit return the sum

# nums=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# even_nums=[]
# for i in nums:
#     if i%2==0:
#         even_nums.append(i)

# squared_list=[]
# for i in even_nums:
#     squared_list.append(i**2)


# print(sum(squared_list))

nums=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

from functools import reduce
even=(list(filter(lambda a:a%2==0,nums)))
square=(list(map(lambda a:a**2,even)))
print((reduce(lambda a,b:a+b,square)))
