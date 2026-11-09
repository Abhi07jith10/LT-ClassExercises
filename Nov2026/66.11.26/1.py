numbers=[1,2,3,4]

new_list=[]

# for i in list:
#     new_list.append(i**2)
# print(new_list)

# [i**2 for i in list]

print(list(map(lambda a: a**2,numbers)))