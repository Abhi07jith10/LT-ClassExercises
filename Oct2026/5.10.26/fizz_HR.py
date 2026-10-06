#if any number is divisible by 3 replace the no and print "fizz"
#if any number is divisible by 5 replace the no and print "buzz"
#if any number is divisible by both 3 aand 5  replace the no and print "fizzbuzz"



i=1
while i<50:
    if i%3==0:
        
        print("fizz")
    elif i%5==0:
        print("buzz")
    elif i%3==0 and i%5==0 :
        print("fizzbuzz")
    else:
        print("")
    i=i+1
    print(i)

print("=====================================")
#for loop

for i in range(1,51):
    if i%3==0 and i%5==0:
        print("fizzbuzz")
    elif i%3==0:
            
            print("fizz")
    elif i%5==0:
            print("buzz")
    else:
         print(i)
    i+=1