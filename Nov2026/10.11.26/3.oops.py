#create a class 
#method 1 :accept a string and return the count of each character in the string
#method 2 :accept a  number and check the number is prime or not
#method 3 :accept a list of numbers and return the sum of even numbers from the list.

class problem():
    def char_count(self,word):
        print({i:word.count(i) for i in word})

    def prime(self,number):
        for i in range(2,number):
            if number%i==0:
                print("not prime")
                break
        else:
            print("prime")

    def evensum(self,numbers):
        print(sum([i for i in numbers if i%2==0]))
    

obj1=problem()
obj1.char_count("hello")
obj1.prime(11)
obj1.evensum([1,2,3,4,5,6,7,8])



