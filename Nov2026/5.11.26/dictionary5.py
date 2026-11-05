students={
    101:{"name":"Arun","age":21,"mark":85},
    102:{"name":"Rahul","age":22,"mark":90},
    103:{"name":"Anu","age":20,"mark":78}
}

list=[]
for i in students:
    list.append(students[i]["mark"])

print(list)

# OR

print([students[i]["mark"] for i in students])