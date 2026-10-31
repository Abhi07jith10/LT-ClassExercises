mobiles={"apple":{"model" : "iphone17","price":160000,"colour":"black"},
         "samsung":{"model" : "S25","price":120000,"colour":"white"},
         "google":{"model" : "pixel","price":80000,"colour":"black"}}


for i in mobiles:
    print(i)  #gets only the keys


print("--------------------------------------------")

for i in mobiles:
    print(mobiles.get(i))   #gets the values
print("--------------------------------------------")

for i in mobiles:
    print(mobiles[i])   #gets the values

print("--------------------------------------------")

for i in mobiles:
    print(mobiles[i]['model'])

print("--------------------------------------------")

for i in mobiles:
    print(mobiles[i]["model"],":",mobiles[i]["colour"])
print("--------------------------------------------")

values={}
for i in mobiles:
    values[i]=[mobiles[i]['model'].mobiles[i]['colour']]

print(values)