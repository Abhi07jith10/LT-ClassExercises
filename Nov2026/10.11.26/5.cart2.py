class Cart:
    def __init__(self, items=None):
        self.items = items if items else {}

    def display_items(self):
        print("Your cart items are:")
        for name, price in self.items.items():
            print(f"{name}: {price}")

    def add_item(self, product_name, price):
        self.items[product_name] = price
        print("The item was added successfully")

    def remove_item(self, product_name):
        if product_name in self.items:
            del self.items[product_name]
            print("The item was removed successfully")
        else:
            print("Item not found in cart")

    def calculate_total(self):
        return sum(self.items.values())



cart = Cart({"mouse": 1000, "keyboard": 2000})
cart.add_item("computer", 200000)
cart.remove_item("mouse")
cart.display_items()
print("Total:", cart.calculate_total())   # Total: 202000
cart.remove_item("laptop")                # Item not found in cart