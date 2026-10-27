#name="aaabbcddd"   #op=a3b2c1d3

name="aaabbcddd" 
new=""
for i in name:
    if i not in new:
      count=name.count(i)
      new+=i+str(count)
print(new);