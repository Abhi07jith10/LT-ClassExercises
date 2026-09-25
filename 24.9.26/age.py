#wap to show that based on specific ages display the things given below
#age=18 or above , display they can vote
#age=17, display that they can learn to drive
#age=16, display that they can buy lottery
#else let them go trick or treating


age=int(input("enter your age: "))

if age>=18:
    print("you can vote")
elif age==17:
    print("you can learn to drive")
elif age==16:
    print("you can buy lottery")
else:
    print("you can go trick or treating")

#note that if i have given if age>18, and i have given input as 18 the op will be trick or treating
