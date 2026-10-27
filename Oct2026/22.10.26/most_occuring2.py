#wap to return the most occuring character from the string given

def most_occuring(word):
        
    largest_count=0
    
    for i in word:
        
        if word.count(i)>largest_count:
            largest_count=word.count(i)

            char=i
        return f"the most occuring character is {char} and the count is {largest_count}"  


print(most_occuring("aaabc"))