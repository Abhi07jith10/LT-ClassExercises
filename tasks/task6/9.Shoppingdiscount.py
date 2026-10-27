#Write a function that accepts the total purchase amount and calculates the final amount after discount:
# • Below ■1,000: no discount
# • ■1,000–■4,999: 5% discount
# • ■5,000 and above: 10% discount
# Return the final payable amount.

def payable_amount(total_amount):
    if total_amount<1000:
        print(f"The final amount is {total_amount}")
    elif total_amount>1000 and total_amount<5000:
        discount_amount=total_amount-total_amount*0.05
        print(f"The payabale amount is {discount_amount}.")
    else:
        discount_amount=total_amount-total_amount*0.1
        print(f"The payabale amount is {discount_amount}.")

payable_amount(5000)


