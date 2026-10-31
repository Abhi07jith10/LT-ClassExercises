#return the mobile model name,brand, price having price between
#80k and 1.5 lakh with black in colour

mobiles={"apple":{"model" : "iphone17","price":160000,"colour":"black"},
         "samsung":{"model" : "S25","price":120000,"colour":"white"},
         "google":{"model" : "pixel","price":80000,"colour":"black"}}

for i in mobiles:
    if mobiles[i]['price']>=80000 and mobiles[i]['price']<=100000:
        print(mobiles[i])