numbers=[1,2,3,4]  #[1,4,9,6]
new_list=[]
for i in numbers:
    squared_num=i**2
    new_list.append(squared_num)
print(new_list)

#using list comprehesnion

print([i**2 for i in numbers])
