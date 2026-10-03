#wap to print the product of even nums between 1 to 10

i=1
product=1

while i<10:
    if i %2==0:
        product=product*i
        print(product)
    i=i+1

print(f"The product is {product}")
