#Remove Characters at Odd Index Positions
# Sample Input: "python"
# Sample Output: "pto"

name = "python"

for i in range(len(name)):
    if i % 2 == 0:
        print(name[i],end='')
        
    