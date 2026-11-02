# Create a nested dictionary containing the price, quantity, and discount percentage of 3 products. Calculate the final
# price of each product after applying the discount.

products = {
 101: {"price": 1000, "quantity": 2, "discount": 10},
 102: {"price": 500, "quantity": 3, "discount": 20},
 103: {"price": 2000, "quantity": 1, "discount": 15}
}

for i in products:
    discount=products[i]["price"]*products[i]["discount"]/100
    print(f"product is {i} and final price is {discount}")