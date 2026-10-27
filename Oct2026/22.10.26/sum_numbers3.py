#wap to get the sum of three number enter by user using functiin


def total(*numbers):
    total=0
    for i in numbers:
        total+=i
    print(total)


total(3,4,5,6)
total(3,4,5)
total(3,4)
