#count lowercase and uppercase letters in a string

string=str(input("enter the string:"))

lower_count=0
upper_count=0
for i in string:
    if i.isupper():
        upper_count+=1
    else:
        lower_count+=1

print(f"the lower count is {lower_count}")
print(f"the upper count is {upper_count}")