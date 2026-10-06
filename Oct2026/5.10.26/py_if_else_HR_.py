#given an integer , perform the following

#If n is odd print"Weird"
#If n is even and in the inclusive range of 2 and 5 print "not weird"
#If n is even and in the inclusive range of 6 and 20 print " weird"
##If n is even and greater than 20 print " weird"


n=int(input("Enter the number : "))

if n%2!=0:
    print("Weird")
elif n%2==0 and n>=2 and n<=5:
    print("Not Weird")
elif n%2==0 and n>=6 and n<=20:
    print(" Weird")
elif n%2==0 and n>20:
    print(" Not Weird")
else:
    print("")

#code redundancy method

if n%2==0:
    print("Weird")
    if n>=2 and n<=5:
      print("Not Weird")
    if n>=6 and n<=20:
      print(" Weird")
    else:
      print(" Not Weird")
else:
    print("Weird")