num=int(input("enter the number : "))

reversed=""

while num>0:
    last_digit=num%10
    string=str(last_digit)
    reversed=reversed+string
    num//=10
print(int(reversed))