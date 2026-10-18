#armstrong

def armstrong(num):
    total=0
    for i in str(num):
        cube=int(i)**3
        total=total+cube

    if total==num:
        print("number is armstrong number.")
    else:
        print("number is not armstrong number.")

armstrong(153)


