name="aaabbcddd"   #op=a3b2c1d3

new=""

for i in name:
    count=name.count(i) 
    if i not in new:   #???????why this step
     new+=i+str(count)    #a3 b2
print(new)
