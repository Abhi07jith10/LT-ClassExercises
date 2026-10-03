#wap to count the digits of a number

number=int(input("enter the number: "))
print(number)
count=0
while number>0:
    number%10
    count+=1

    number//=10  #we need to decrement the numbers, for ex5678, 567, 56, 5

print(f"The total count is {count}")

