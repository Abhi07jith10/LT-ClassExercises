# Write a function that accepts a number and a digit. Return how many times that digit appears in the number.
# Example: Number = 1223122, Digit = 2 → 4


def freq_analyzer():
    number=int(input("enter the number :"))
    digit=int(input("enter the digit :"))
    count=0
    for i in str(number):
        if i==str(digit):
            count+=1
    print(count)

freq_analyzer()