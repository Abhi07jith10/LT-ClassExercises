#1. BMI Calculator
#Write a Python program to calculate the Body Mass Index (BMI). Take the person's weight in kilograms
#and height in metres as input.

weight=float(input("enter the weight in kg : "))
height=float(input("enter the height in metres: "))
BMI=weight/height**2

print(f"The BMI of the person is : {BMI}")
