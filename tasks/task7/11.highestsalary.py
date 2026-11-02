# Find the employee who receives the highest salary without using the max() function.


employees = {
 101: {"salary": 25000},
 102: {"salary": 45000},
 103: {"salary": 35000},
 104: {"salary": 50000}
}

highest_salary=0
for i in employees:

    if employees[i]["salary"]>highest_salary:
        highest_salary=employees[i]["salary"]

print(f"Employee id:{i}")
print(f"salary is {highest_salary}")