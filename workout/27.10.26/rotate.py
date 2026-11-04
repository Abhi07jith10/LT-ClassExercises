# Rotate a list
# Given ip = [1, 2, 3, 4, 5, 6] 
# and k = 2, 
# Expected: [5, 6, 1, 2, 3, 4]


numbers=[1, 2, 3, 4, 5, 6,7]

new=[]
k=2
first=len(numbers)-k  #4
for i in range(first+1):
    if i in numbers:
     numbers.remove(i)
     numbers.append(i)
print(numbers)




        
    



