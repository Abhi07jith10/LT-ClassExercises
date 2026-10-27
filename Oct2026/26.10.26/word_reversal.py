text="python is a programming language."

words=text.split()

words.reverse()
reverse=""

for i in words:
    reverse+=i+" "
print(reverse)