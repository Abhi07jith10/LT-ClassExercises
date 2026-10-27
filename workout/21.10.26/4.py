#Accept a starting number and an ending number. 
# Display all Armstrong numbers within that range.

start_num= int(input("enter the start number : "))
stop_num= int(input("enter the stop number: "))


for i in range(start_num,stop_num+1,1):
    total=0
    for j in str(i):
        cube=int(j)**3
        total+=cube
    if total==i:
        print(i)
    