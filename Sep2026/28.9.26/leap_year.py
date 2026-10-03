#leap year

#century years : divisible by 400 
#non century years: divisible by 4 but not by 100

year=int(input("enter the year: "))

if year%400==0 or (year%4==0 and year%100!=0):
    print(f"The {year} is a leap year")
else:
    print(f"The {year} is not leap year.")

