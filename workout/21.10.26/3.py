#3. Write a program to count how many 
# Armstrong numbers exist between 1 and n.

n=int(input("enter the range : "))
count=0
for i in range(1,n+1):
    total=0
    for j in str(i):
        cube=int(j)**3
        total+=cube
    if total==i:
        print(i)
        count+=1
print(f"count is {count}")