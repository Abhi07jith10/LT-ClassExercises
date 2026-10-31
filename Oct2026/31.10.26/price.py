#return the mobiles having price more than one lakh

mobiles={"apple":{"model" : "iphone17","price":160000,"colour":"black"},
         "samsung":{"model" : "S25","price":120000,"colour":"white"},
         "google":{"model" : "pixel","price":80000,"colour":"black"}}

for i in mobiles:
    if mobiles[i]['price']>100000:
        print(mobiles[i]['model'])