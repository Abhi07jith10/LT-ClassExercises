#armstrong num is the num in which the number that equals to the sum of its own digits
#where each digit is raised to the power of the total number of digits

#ex.3 digit number: 153>>> 1³ = 1 × 1 × 1 = 1 ,5³ = 5 × 5 × 5 = 125 ,3³ = 3 × 3 × 3 = 27 
# 1+125+27=153
#370======, 3³ = 27, 7³ = 343, 0³ = 0 , 27 + 343 + 0 = 370  


num=int(input("enter the number: "))
temp=num
length=len(str(num))

total=0

while(num>0):
    last_digit=num%10
    cube=last_digit**length
    total=total+cube

    num//=10

if total==temp:
    print(f"Number {temp} is armstrong")
else:
    print(f"Number {temp} is not armstrong")




    