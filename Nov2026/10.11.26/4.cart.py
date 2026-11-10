#create a class CART
#method 1: display the cart items enter by user
#method 2:Add item
#method 3:remove item
#method 4 :calculate the total

class Cart():
    def display_items(self,items):
        self.items=items
        print("Your cart items are")
        print(items)

    def add_item(self,product_name,price):
        self.items[product_name]=price
        print("the item added succesfully")

    def remove_item(self,product_name):
        del self.items[product_name]
        print("The item removed succesfully")

    def total_product(self):
        print(F"the total number of products is {len(self.items)}")
        print(F"the total price of all products is {sum(self.items.values())}")
obj1=Cart()
obj1.display_items({"mouse":1000, "keyboard":2000})
obj1.add_item("computer",200000)
obj1.remove_item("mouse")
