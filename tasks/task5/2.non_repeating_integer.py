#. Find the First Non-Repeating Character
# Sample Input: "aabbcddee"
# Sample Output: "c"

string="aabbcddee"

for i in string:
    if string.count(i)==1:
        print(i)
        break

