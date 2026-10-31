string="python is a programming language"

new_string=string.split()
largest_word=0
for i in new_string.copy():
    if (len(i))>largest_word:
        largest_word=len(i)
        word=i
print(word)