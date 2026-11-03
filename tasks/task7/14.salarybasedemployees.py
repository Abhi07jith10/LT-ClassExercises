# Create a nested dictionary containing the details of 4 employees. Display the employees whose salary is greater
# than ■30,000.


employees = {
 101: {"salary": 25000, "experience": 2},
 102: {"salary": 40000, "experience": 5},
 103: {"salary": 35000, "experience": 3},
 104: {"salary": 28000, "experience": 1}
}

for i in employees:
    if employees[i]["salary"]>30000:
        print(f"employee id:{i} , salary:{employees[i]["salary"]}")