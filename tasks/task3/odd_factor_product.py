#odd_product
# wap to get the product of odd factore of the number entered

num=int(input("enter the number : "))

i=1
total=1

while i<=num:
    if num%i==0 and i%2!=0:
        total=total*i
    i+=1
print(f"The total product of the odd factors of the given number is {total}")
