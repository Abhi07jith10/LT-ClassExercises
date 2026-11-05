students={
    101:{"name":"Arun","age":21,"mark":85},
    102:{"name":"Rahul","age":22,"mark":90},
    103:{"name":"Anu","age":20,"mark":78}
}

highest=0
for i in students:
    if students[i]["mark"]>highest:
        highest=students[i]["mark"]

print(highest)

