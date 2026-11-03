#Create a nested dictionary representing a shopping cart. Each product contains its price and quantity. Calculate
# the total bill amount.


cart = {
 101: {"price": 100, "quantity": 3},
 102: {"price": 250, "quantity": 2},
 103: {"price": 500, "quantity": 1}
}

total_amount=0
for i in cart:
    total_amount+=cart[i]["price"]*cart[i]["quantity"]

print(total_amount)