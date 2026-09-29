#even factors sum
# Wap to the count of even factors of a number enter

num=int(input("enter the number : "))

i=1
total=0

while i<=num: 
    if num%i==0 and i%2==0:
        
        total=total+1
    i=i+1
print(f"the total count of the even factors of the given number is {total}")