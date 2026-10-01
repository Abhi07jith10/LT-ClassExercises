#wap to get the sum of digits in a number

number=int(input("enter the number: "))

total=0
while number>0:
    last_digit=number%10
    
    total+=last_digit
    number//=10
print(f"the total sum of the digit is {total}")
