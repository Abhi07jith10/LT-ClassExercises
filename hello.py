#input:"hello"
#output:
# h:1
# e:1
# l:2
# o:1

string="hello"
new=""

for i in string:
    if i not in new:
        new+=i
        print(f"{i}:{string.count(i)}")





     
    
