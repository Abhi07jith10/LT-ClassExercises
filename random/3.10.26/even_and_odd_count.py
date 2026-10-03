#Count Even and Odd Digits Separately — 
# Take a number and count how many of its digits are even and how many are odd.

num=int(input("enter the num: "))

odd_count=0
even_count=0
temp=num

while num>0:
    last_d=num%10
    if last_d%2==0:
        even_count+=1
    if last_d%2!=0:
        odd_count+=1
    num//=10
print(f"The odd count of the number {temp} is {odd_count} and even count is {even_count}")