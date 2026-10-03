#Sum of Alternate Digits — 
# Take a number and find the sum of digits at odd positions only (1st, 3rd, 5th... from the right).

num=int(input("enter the number : "))
total=0

i=1
while num>0:
    last_d=num%10
    if i%2!=0:
        total=total+last_d
    num//=10
    i+=1

print(total)