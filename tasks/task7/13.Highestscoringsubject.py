# Create a nested dictionary containing the marks of 3 students in 3 subjects. Find the subject in which each student
# scored the highest marks.

students = {
 101: {"Maths": 80, "Physics": 95, "Chemistry": 75},
 102: {"Maths": 90, "Physics": 85, "Chemistry": 95},
 103: {"Maths": 70, "Physics": 80, "Chemistry": 65}
}

highest_subject_marks_M=0
highest_subject_marks_P=0
highest_subject_marks_C=0

for i in students:
    if (students[i]["Maths"])>highest_subject_marks_M:
        highest_subject_marks=(students[i]["Maths"]) 
        print(i,f"Highest subject is {(students[i]["Maths"]) }")
    
    if (students[i]["Physics"])>highest_subject_marks_P:
        highest_subject_marks_P=(students[i]["Physics"])
        print(i,f"Highest subject is {(students[i]["Physics"]) }")


    if (students[i]["Chemistry"])>highest_subject_marks_C:
        highest_subject_marks_C=(students[i]["Chemistry"])
        print(i,f"Highest subject is {(students[i]["Chemistry"]) }")
  