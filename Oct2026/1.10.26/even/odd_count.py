#wap to generate the count of even and odd numbers in py

n=int(input("enter the number: "))
even_count=0        
odd_count=0

for i in range(1, n+1):
    if i%2==0:
        even_count+=1
    else:
        odd_count+=1

print(f"The even count of numbers is {even_count} and odd count of numbers is {odd_count}")