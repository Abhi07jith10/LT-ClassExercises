#wap to check the given no is positive or negative

num=int(input("enter the number:"))

if num>0:
    print(f"the entered number {num} is positive")

elif num==0:
    print(f"the number {num} is either positive nor negative")

else:
    print(f"the entered number {num} is negative")


#In this question if we give input as zero then the output will be negative
# because 0>0 is false and it will jump onto the else statement ehrefore the op will be negative
#therefore we can use elif block inside else and if
#note that we can give "n" no of elif blocks inside else and if.