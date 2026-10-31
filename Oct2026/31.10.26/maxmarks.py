#find maxm marks of Arun

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


for i in students:
    if students[i]["name"]=="Arun":
        print(max(students[i]['marks']))

for i in students:
    if students[i]["name"]=="Arun":
        print(students[i]["name"],max(students[i]['marks']))

