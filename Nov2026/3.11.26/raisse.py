age=int(input("enter the number:"))
if age<=18:
    raise Exception("Not eligible")
else:
    print("you are eligible.")
