# Create a nested dictionary containing the marks of 3 students in 3 subjects. Calculate the total marks of each
# student.


students = {
 101: {"Maths": 80, "Physics": 75, "Chemistry": 90},
 102: {"Maths": 65, "Physics": 85, "Chemistry": 70},
 103: {"Maths": 90, "Physics": 95, "Chemistry": 85}
}

for i in students:
    total=students[i]["Maths"]+students[i]["Physics"]+students[i]["Chemistry"]
    print(i,":",total)

