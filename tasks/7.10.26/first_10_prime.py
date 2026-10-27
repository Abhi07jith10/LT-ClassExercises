# get the  first 10 prime numbers from 1 to n

n=int(input("enter the number : "))   #1 to 100

while n<=1:
    print("Please enter a number that is greater than 1")
    n=int(input("enter the number : "))   #1 to 200

count=0
for num in range(2,n):
    
    for i in range(2,num):
          if num%i==0:
              
              break
    
    else:
        print(f"number {num} is prime")
        count=count+1
        if count==10:
            break
         