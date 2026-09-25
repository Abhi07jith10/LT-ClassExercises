#wap to enter the students marks, if grade is between 91 and 100 grade will be A
#81-90 grade will be B
#71-80 grade will be C
#61-70 grade will be C
#below 60 grade will be failed

mark=int(input("enter the marks: "))

if mark>=91 and mark<=100:
    print("The student's grade is A")
elif mark>=81 and mark<=90:
    print("The student's grade is B")
elif mark>=71 and mark<=80:
    print("The student's grade is C")
elif mark>=61 and mark<=70:
    print("The student's grade is D")

else:
    print("The student has failed .")



