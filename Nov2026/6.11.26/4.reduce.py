numbers=[1,2,3,4,5,6]

from functools import reduce
print(reduce(lambda a,b: a+b,numbers))

#a=2 , b=2 ---- a+b=4
#a=4 , b=3 ---- a+b=7
#a=7 , b=4 ---- a+b=11

