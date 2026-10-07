#wap to print the numbers from 10 to 200

for num in range(10,200): #10
    for i in range (2,num):  #now num=10, so the loop goes from (2,10)
        if num%i==0:   # 10%2==0

           break  
    else:
     print(f"The number {num} is prime")