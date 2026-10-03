#get the factors of the number given
#8:1,2,4,8
#6:1,2,3,6

n=int(input("enter the number"))

for i in range(1,n+1):
    if n%i==0:
        print(i)
