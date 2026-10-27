# 5. Electricity Bill Calculator
# Write a function that accepts the number of electricity units consumed and calculates the bill using these
# slabs:
# • First 100 units: ■2 per unit
# • Next 100 units: ■3 per unit
# # • Units above 200: ■5 per unit
# # Return the total bill amount. Apply each rate only to the units in its slab

def electricitybill():
    units=int(input("enter the unit consumed: "))

    if units <=100:
        bill=units*2
    elif units<=200:
        bill=100*2+ (units-100)*3
    else:
        bill=100*2+ 100*3 + (units-200)*5

    print(f"The total bill amount is {bill}")

electricitybill()
