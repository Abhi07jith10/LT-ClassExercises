# Create a nested dictionary containing the details of 3 employees. Display the salary of the second employee.
employees = {
 101: {"age": 25, "salary": 25000, "experience": 2},
 102: {"age": 30, "salary": 40000, "experience": 5},
 103: {"age": 28, "salary": 35000, "experience": 3}
}

for i in employees:
    if i==102:
        print(employees[i]["salary"])