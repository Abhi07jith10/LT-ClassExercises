#wap to reverse a number enter by user

num=int(input("enter the number: "))
temp=num
new_no=""

while num>0:
    last_digit=num%10
    string=str(last_digit)
    new_no=new_no+string
    num//=10
    integer=int(new_no)

print(f"the reversed number of the entered number {temp} is {integer}")



