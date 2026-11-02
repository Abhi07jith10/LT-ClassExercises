# Calculate the sum of the diagonal elements in a 3×3 matrix.

matrix = [
 [10, 20, 30],
 [40, 50, 60],
 [70, 80, 90]
]

new=[]
for i in matrix:
    for j in i:
        new.append(j)


total=new[0]+new[4]+new[8]
print(total)

        