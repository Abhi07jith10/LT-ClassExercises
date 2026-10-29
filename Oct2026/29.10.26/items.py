elements={"name":"Abhi","age":22,"place":"tvm"}
#op=[(name:age),(age:27),(place:tvm)]
items=[]
for i in elements:
    items.append( ((i,elements[i])))

print(items)

print((i,elements[i]) for i in elements)  #comprehension method