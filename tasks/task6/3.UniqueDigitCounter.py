#Write a function that accepts an integer and returns the number of distinct digits present in it.
# Example: 12234521 → 5


def distinct(num):
    
    
    new=""
    count=0
    for i in str(num):
        if i not in new:
            new+=i
    print(len(new))

distinct(112233445566)



