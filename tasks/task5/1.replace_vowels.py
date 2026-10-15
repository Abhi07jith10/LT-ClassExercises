# Replace Vowels with *
# Sample Input: "education"
# Sample Output: "*d*c*t**n"

string="education"

vowels="aeiou"

new=""
for i in string:
    if i in vowels:
        new=new+"*"
    else:
        new=new+i


print(new)
