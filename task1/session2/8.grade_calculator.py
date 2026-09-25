#. Grade Calculator
#Write a Python program that accepts a student's mark. If the mark is 90 or above, display grade A. If the
#mark is 75 or above, display grade B. If the mark is 50 or above, display grade C. If the mark is 40 or
#above, display grade D. Otherwise, display Fail.

mark=int(input("enter the students marks: "))

if mark>=90:
    print (f"The grade of the student is A")
elif mark>=75:
    print(f"The grade of the students is B")
elif mark>=50:
    print(f"The grade of the students is C")
elif mark>=40:
    print(f"The grade of the students is D")
else:
    print("The student has failed.")


