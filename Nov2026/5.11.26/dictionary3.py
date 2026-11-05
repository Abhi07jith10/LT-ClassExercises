students={
    101:{"name":"Arun","age":21,"mark":85},
    102:{"name":"Rahul","age":22,"mark":90},
    103:{"name":"Anu","age":20,"mark":78}
}
#print age and mark of all student

for i in students:
    print(students[i]["age"],students[i]["mark"])