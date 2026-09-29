#Temperature Category
#Write a Python program that accepts a temperature. If the temperature is above 30, display "Hot". If the
#temperature is below 20, display "Cold". Otherwise, display "Normal".

Temperature=float(input("Enter the temperature : "))

if Temperature>30:
    print("The current temperature is hot.")
elif Temperature<20:
    print("The current temperature is cold.")
else:
    print("The temperature is normal.")

    