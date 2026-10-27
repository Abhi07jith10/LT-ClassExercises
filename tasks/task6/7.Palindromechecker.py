# Write a function that accepts an integer and returns True if the number reads the same forward and
# backward; otherwise, return False.
# Example: 12321 → True; 12345 → False

def palindrome(number):
    
    new=""
    temp=number
    while number>0:
        last_digit=number%10
        new+=str(last_digit)
        number//=10

    print(new)
    if (temp)==int(new):
        print("True")
    else:
        print("False")


palindrome(12321)

    