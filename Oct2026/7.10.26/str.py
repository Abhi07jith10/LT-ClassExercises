for num in range(10,500):
    total=0
    for j in str(num):
        fact=1
        if int(j)==0 or 1:
            fact=1
        else:
            for k in range(1, int(j)+1):
                fact*=k

            total+=fact
    if total==fact:
            print(f"number {num} is a strong number.")