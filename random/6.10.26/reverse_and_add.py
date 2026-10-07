#Reverse and Add (Check if Result is Palindrome) —
#  Take a number, reverse it, add the reverse to the original number, and check if the result is a palindrome.
#Reverse it: 59 → 95
# Add: 59 + 95 = 154
# Reverse 154: 451 — not equal to 154, so not a palindrome.

# One where it works — take 23:

# Reverse it: 23 → 32
# Add: 23 + 32 = 55
# Reverse 55: 55 — same as original, so 55 is a palindrome. 

#139:

# Reverse: 139 → 931
# Add: 139 + 931 = 1070
# Reverse 1070: 0701 → not equal → not a palindrome

num=int(input("enter the number : "))  
rev=0
temp=num

while num>0:
    last_digit=num%10
    rev=rev*10 + last_digit
    num//=10

total=temp+rev
rev_t=0

temp_total=total

while total>0:
    last_digit_t=total%10
    rev_t=rev_t*10 + last_digit_t
    total//=10

if rev_t==temp_total :
    print("number is palindrome")
else:
    print("Number is not palindrome")









