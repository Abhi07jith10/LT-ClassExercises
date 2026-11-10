#create a class 
#method 1 :accept a string and return the count of each character in the string
#method 2 :accept a  number and check the number is prime or not
#method 3 :accept a list of numbers and return the sum of even numbers from the list.

class problem():
    def char_count(self,word):
        new=""
        for i in word:
            if i not in new:
                new+=i

        for j in new:
            print(f"{j}-{word.count}")

    def prime(self,number):
        for i in range(2,number):
            if number%i==0:
                print("not prime")
                break
        else:
            print("prime")

    def evensum(self,numbers):
        new=[]
        for i in numbers:
            if i%2==0:
                new.append(i)
            
        print(f"The total sum of even numbers is {sum(new)}")

obj1=problem()
obj1.char_count("hello")
obj1.prime(11)
obj1.evensum([1,2,3,4,5,6,7,8])



