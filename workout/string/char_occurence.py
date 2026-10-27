#return the character that occurs most in the given string

string=str(input("enter the string: ")) #aaaaabbc

largest_count=0
char=""
for i in string:
    if string.count(i)>largest_count:
        largest_count=string.count(i)
        char=i
print(f"the largest count letter is {char} and count is {largest_count}")