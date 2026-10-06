#A strong number (also known as a Krishnamurthy number or Factorion) 
# is a number where the sum of the factorials of its individual digits is equal to the number itself.
#For example, 145 is a strong number because:
# (1!+4!+5!=1+24+120=145)

number=645
total=0

for i in str(number):

    fact=1
    
    for j in range(1,int(i)+1):     # int("6") + 1  6 + 1
        fact*=j
    total+=fact

if total==number:
    print(f"The number {number} is a strong number.")

else:
    print(f"The number {number} is not a strong number.")


