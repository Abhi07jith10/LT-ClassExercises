#Expand an Encoded String
# Sample Input: "a3b2c4"
# Sample Output: "aaabbcccc"


string="a3b2c4"
new=""
letter=""
for i in string:
      if i.isalpha():
          letter=i
      elif i.isdigit():
          digit=int(i)
          new+=letter*digit
print(new)

word="a3b2c4"
new=""

for i in range(len(word)):
     if word[i].isdigit():
          new+=word[i-1]*int(word[i])
print(new)