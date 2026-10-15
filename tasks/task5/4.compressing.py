#. Compress a String
# Sample Input: "aaabbccccdaa"
# Sample Output: "a3b2c4d1a2

string="aaabbccccdaa"

compressed=""
count=1

for i in range(1, len(string)):
    if string[i]==string[i-1]:
        count+=1
    else:
        compressed+= string[i-1]+str(count)
        count=1
    compressed+=str+str(count)

print(compressed)

