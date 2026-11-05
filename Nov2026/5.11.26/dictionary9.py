# add a new mark of 100 to lsit of rahul

students={
    "Arun":[85,90,78,92],
    "Rahul":[70,65,80,75],
    "Anu":[95,88,92,88]

}

for i in students:
    if i=="Rahul":
        students[i].append(100)

print(students)