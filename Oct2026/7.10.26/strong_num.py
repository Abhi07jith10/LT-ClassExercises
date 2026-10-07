#A Strong Number (also called a Krishnamurthy number or a factorial chain number) is a positive integer where the sum of the factorials of its digits equals the number itself.
#Example
#Take the number 145:
# Find the factorial of each digit:
#	• 1! = 1
#	• 4! = 24
#	• 5! = 120

#• Add them together: 1 + 24 + 120 = 145.
#Since the sum matches the original number, 145 is a Strong Number.

for num in range(1,500):
    temp=num
    total=0
    for i in range(1,num):
        last_d=num%10
        fact=1
        total=0
        
        for j in range(1,last_d):
           if last_d%i==0:
             fact=fact*i
             total=total+fact
        if total==temp:
           print(f"Num  {num}is a strong number")

