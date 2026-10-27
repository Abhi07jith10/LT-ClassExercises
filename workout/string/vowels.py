#count of vowels

vowels="AEIOUaeiou"

name=str(input("enter the name: "))
count=0
for i in name:
    if i in vowels:
        count+=1
print(count)