# Display the elements of a nested list column by column using nested loops.

numbers = [
 [10, 20, 30],
 [40, 50, 60],
 [70, 80, 90]
]

new=[]
for i in numbers:
    for j in i:
        new.append(j)

print(new[0],new[3],new[6])
print(new[1],new[4],new[7])
print(new[2],new[5],new[8])

