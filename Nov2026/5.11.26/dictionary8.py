students={
    "Arun":[85,90,78,92],
    "Rahul":[70,65,80,75],
    "Anu":[95,88,92,88]

}


#return total marks
new_list=[]

for i in students:
    total=sum(students[i])
    new_list.append(total)

print(new_list)

#list comprehension

print([sum(students[i])])