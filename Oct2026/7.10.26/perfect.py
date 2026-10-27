""""""
#A perfect number is a positive integer that equals the sum of its proper divisors, excluding the number itself.

#Examples of Perfect Numbers

# 6: Proper divisors are 1, 2, and 3. Their sum (1 + 2 + 3) equals 6.
# 28: Proper divisors are 1, 2, 4, 7, and 14. Their sum equals 28.

""""""



for num in range(1,501):
    total=0
    
    for j in range(1,num):
    
      if num%j==0:

        total+=j
    
    


    if total==num:
      print(f"number {num} is a perfect number.")