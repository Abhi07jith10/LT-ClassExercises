#Write a function that accepts an integer and returns the number formed by arranging its digits in ascending order.
# Example: 583214 → 123458

def num_reorder(num):
    digits=str(num)
    new=""

    for i in range(0,10):
        for j in digits:
            if int(j)==i:
                new+=j
    return int(new)

print(num_reorder(6105321))