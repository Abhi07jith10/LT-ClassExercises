#Digital Root Without Repeating the Whole Process — 
# Find the single-digit sum of a number's digits, but this time track and display how many "rounds" of digit-summing it took to get there.

#Take the number 9875.

# Round 1: Add its digits: 9 + 8 + 7 + 5 = 29. That's a 2-digit number, so you're not done — round count so far = 1.

# Round 2: 29 is still more than one digit, so add its digits: 2 + 9 = 11. Still 2 digits — round count = 2.

# Round 3: Add again: 1 + 1 = 2. Now it's a single digit — stop here. Round count = 3.

# Final answer: Digital root = 2, achieved in 3 rounds.

num=999999999
total=0

while total>9:
    new_total=0
    temp=total
    while temp>0:
        last_digit=temp%10
        new_total = new_total+last_digit
        temp//=10
    total=new_total
    rounds+=1


