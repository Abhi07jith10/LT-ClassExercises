#wap to get the count of vowels from the string

name="HElloworld"
vowels="aeiouAEIOU"

count=0
for i in name:
    if i in vowels:
        count+=1
print(f"the total count of vowels is {count}")