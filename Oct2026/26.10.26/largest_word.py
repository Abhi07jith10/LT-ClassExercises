#wap to enter the largest word from the string enter by user

text="python is the programming language"

words=text.split()
largest=0
for i in words:
    if len(i)>largest:
        largest=len(i)
        word=i
print(word)   