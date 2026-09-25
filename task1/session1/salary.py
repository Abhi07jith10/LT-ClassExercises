# Salary Calculator
#Write a Python program to calculate HRA, DA, and gross salary from a given basic salary.
#Equations:
#HRA = Basic Salary × 10 / 100
#DA = Basic Salary × 5 / 100
#Gross Salary = Basic Salary + HRA + DA

Basic_salary=int(input("Enter the basic salary amount : "))

HRA=(Basic_salary*10)/100
DA=(Basic_salary*5)/100
Gross_Salary=Basic_salary+HRA+DA

print(f"The HRA of the person is {HRA}")
print(f"The DA of the person is {DA}")
print(f"The Gross Salary of the person is {Gross_Salary}")

