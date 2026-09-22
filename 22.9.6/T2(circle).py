#Find the area and circumference of a circle


radius=int(input("enter the radius: "))  #int or float
pi=3.14
circumference= 2*pi*radius
area=pi*(radius*radius)  #or (area=pi*r**2)

print(f"circumference is {circumference}")
print(f"area is {area}")

