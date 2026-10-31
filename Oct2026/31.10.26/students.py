students = {
    "student1": {
        "name": "Arun",
        "marks": [80, 90, 95]
    },
    "student2": {
        "name": "Anu",
        "marks": [70, 80, 95]
    },
    "student3": {
        "name": "Ajay",
        "marks": [60, 90, 75]
    }
}

#add 100 to the marks of anu

for i in students:
    if students[i]["name"]=="Anu":
        students[i]["marks"].append(100)

print(students)