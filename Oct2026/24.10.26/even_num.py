#print even numbers from 1 to 50 and add them in a list

numbers=[]
for i in range(1,51):
    if i %2==0:
        numbers.append(i)

print(numbers)
