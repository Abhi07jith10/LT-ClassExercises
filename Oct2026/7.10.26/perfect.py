for num in range(1,501):
    total=0
    
    for j in range(1,num):
    
      if num%j==0:

        total+=j
    
    


    if total==num:
      print(f"number {num}is a perfect number.")