# #6. Password Strength Checker
# Write a function that accepts a password and returns its strength based on these conditions:
# • Weak: fewer than 8 characters
# • Medium: at least 8 characters but missing either an uppercase letter or a digit
# • Strong: at least 8 characters and contains both an uppercase letter and a digit.
def password_strength(password):
    cap_letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    small_letters="abcdefghijklmnopqrstuvwxyz"


    if len(password)<8:
        print("Password is weak")
    else:
        for i in password:
            if i not in cap_letters or i.isalnum()==False:
                print("Password is medium")
                break
            elif i in cap_letters and i.isalnum()==True:
                print("Password is strong")
                break

password_strength("aaaaBBBC2024")