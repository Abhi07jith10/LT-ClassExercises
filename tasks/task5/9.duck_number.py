# Check Duck Number
# Sample Input: 1023
# Sample Output: Duck Number
# Sample Input: 1234
# Sample Output: Not a Duck Number

#Zero must come anywehere after the frist digit

num=1023
string=str(num)

# if string[1]==str(0):
#     print("number is duck number")

num = 1023
string = str(num)

for i in range(1, len(string)):
    if string[i] == "0":
        print(f"The number {num} is a Duck number")
        break
else:
    print(f"The number {num} is not a Duck number")
