#get the length and breadth of a rectangle and calculate its area and perimeter
length=int(input("enter the length: "))
breadth=int(input("enter the breadth: "))
area=length*breadth
perimeter= 2*(length+breadth)

print(f"the area is {area}")
print(f"the perimeter  is {perimeter}")

#Note that if we give float instead of int , and suppose we given input as 10, the op will be ex>62.00000000000002,
#here the 2 came because atlast value cant be converted to binary digits so next nearest value is pasted there.



