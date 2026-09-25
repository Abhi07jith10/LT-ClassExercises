#Ask the user if it is raining  If they answer “yes”, 
# ask if it is windy. If they answer “yes” to this second question, 
# display the answer “It is too windy for an umbrella”, otherwise 
# display the message “Take an umbrella”. If they did not answer yes 
# to the first question, display the answer “Enjoy your day”.

is_rainy=input("Is it raining???????? ")

if is_rainy=="yes" :
    is_windy=input("Is it windy there: ")
    if is_windy=="yes":
        print("It is too windy for an umbrella.....")
    else:
        print("Take an umbrella....")
else:
    print("Enjoy your day.....")
