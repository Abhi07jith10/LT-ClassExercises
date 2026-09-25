#7. Discount Calculator
#Write a Python program that accepts a purchase amount. If the amount is ■5000 or above, give a 20%
#discount. If the amount is ■2000 or above, give a 10% discount. Otherwise, there is no discount. Display
#the discount amount and the final amount.
#Equations:
#Discount = Amount × Discount Rate / 10
#Final Amount = Amount − Discount

Amount=float(input("Enter the purchase amount: "))

if Amount>=5000:
    discount_amount=(Amount*0.2)/10
    final_amount=Amount-discount_amount
    print(f"The discount amount is {discount_amount}")
    print(f"The Final amount is {final_amount}")


elif Amount>=2000 :
    discount_amount=(Amount*0.1)/10
    final_amount=Amount-discount_amount

    print(f"The discount amount is {discount_amount}")
    print(f"The Final amount is {final_amount}")


else:
    discount_amount=(Amount*0)/10
    final_amount=Amount-discount_amount
    
    print(f"The discount amount is {discount_amount}")
    print(f"The Final amount is {final_amount}")




