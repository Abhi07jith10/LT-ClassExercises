#sample ip:aaabbcc
#sample op: b

str1 = input("Enter the string: ")
mostcount = 1
scount = 1
scountchar = ""

for i in str1:
  if str1.count(i)>mostcount and str1.count(i)>scount:
    scount = mostcount
    mostcount = str1.count(i)

  elif str1.count(i)<mostcount and str1.count(i)>scount:
    scount = str1.count(i)
    scountchar = i

  else:
    pass

print(f"Second frequent char is {scountchar}")




