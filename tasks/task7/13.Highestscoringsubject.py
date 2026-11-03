# Create a nested dictionary containing the marks of 3 students in 3 subjects. Find the subject in which each student
# scored the highest marks.

students = {
 101: {"Maths": 80, "Physics": 95, "Chemistry": 75},
 102: {"Maths": 90, "Physics": 85, "Chemistry": 95},
 103: {"Maths": 70, "Physics": 80, "Chemistry": 65}
}

for i in students:
    highest_mark=0
    best_subject=""
    for k in students[i]:
        if students[i][k]>highest_mark:
            highest_mark=students[i][k]
            best_subject=k
    print(f"student {i} scored highest in {best_subject} ({highest_mark})")

  