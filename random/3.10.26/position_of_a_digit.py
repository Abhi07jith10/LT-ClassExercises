#Find the Position of a Digit — 
# Take a number and a target digit, and find at which position (from the right, starting at 1) that digit first appears.

num=int(input("enter the number: "))
temp=num
target_digit=int(input("enter the target digit :"))


i=1
while num>0:
    last_d=num%10
    if last_d==target_digit:
        print(f"The target digit is {i} position from right side of the number {temp}")
        break
    
    i+=1
    num//=10

else:
    print("Target digit not found.")



