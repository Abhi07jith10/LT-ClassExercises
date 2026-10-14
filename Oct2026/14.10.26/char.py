#Ask the user to enter their first name. If the length  of their first name is under five characters, ask 
# them to enter their surname and join them  together (without a space) and display the name 
# in upper case. If the length of the first name is five  or more characters, display their first name in lower case.

name=input(str("enter the name: "))

if len(name)<5:
    sur_name=str(input("enter the surname :  "))
    new_name=name+sur_name
    capitalize_name=new_name.upper()
    print(capitalize_name)
else:
    lower=name.lower()
    print(lower)
