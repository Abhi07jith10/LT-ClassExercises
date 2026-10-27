#Write a function that accepts an integer and returns a new number formed by replacing every even digit with
# 0 and every odd digit with 1.
# Example: 583246 → 101010

def transformation(num):
    new=""
    for i in str(num):
        if int(i)%2==0:
            new+="0"
        else:
            new+="1"
    print(new)

transformation(123456)


