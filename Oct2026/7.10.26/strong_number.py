for num in range(10,500):
    total=0
    for j in str(num):
        fact=1
        for k in range(1,int(j)+1):
            fact*=k
        total+=fact
    if total==fact:
        print(f"the number {num} is a strong number.") 