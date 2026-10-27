#145 is a strong number because:
# (1!+4!+5!=1+24+120=145)

num=145
temp=num
total=0
while num>0:  # 145>0
    last_d=num%10   
    fact=1
    
    for i in range(1,last_d+1):
        fact=fact*i  
    total=total+fact  
        
    num//=10

if total==temp:
    print("the number is a strong number")
else:
    print("not a strong num")


    


    



