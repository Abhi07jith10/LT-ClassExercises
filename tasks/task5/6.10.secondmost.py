str1 = input("Enter the string: ")
mostcount = 0
secondmostcount = 0
secondcountchar = str1[0]

for i in str1:
  if str1.count(i) > mostcount:
    mostcount = str1.count(i)

for i in str1:
  if str1.count(i) < mostcount and str1.count(i) > secondmostcount:
    secondmostcount = str1.count(i)
    secondcountchar = i

print(f"Second frequent char is {secondcountchar}")