#wap to get the total count of vowels from the string enter by user

def count_vowels(word):
    vowels="aeiou"
    count=0

    for i in word.lower():
        if i in vowels:
            count+=1

    return count

string=input("enter the word: ")
print(count_vowels(word=string))

#return : statement inside a function to send a specific output or result
#or value back to the function caller line.