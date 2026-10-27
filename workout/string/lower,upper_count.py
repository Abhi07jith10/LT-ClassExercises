#count lowercase and uppercase letters in a string

name="ABHIjith"
upper_count=0
lower_count=01

for i in name:
    if i.isupper():
        upper_count+=1
    else:
        lower_count+=1
    
print(f"the lower count is {lower_count}")
print(f"the upper count is {upper_count}")

