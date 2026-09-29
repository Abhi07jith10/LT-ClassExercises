#6. Simple Interest Calculator
#Write a Python program to calculate simple interest. Take the principal amount, annual rate of interest,
#and time in years as input.
#Equation: Simple Interest = (P × R × T) / 100
#where P = Principal, R = Rate, T = Time

Principal=float(input("enter the principal amount: "))
Rate_of_interest=float(input("enter the Rate of interest: "))
Time=float(input("enter the time in years: "))

Simple_interest= (Principal*Rate_of_interest*Time)/100
print(f"The simple interest is {Simple_interest}")

