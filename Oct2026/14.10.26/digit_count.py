#count the number of digits in a string

word="Abc123"

count=0
for i in word:
    if i.isdigit():
        count+=1  
print(count)

