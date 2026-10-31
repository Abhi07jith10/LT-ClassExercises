# input="python"
# output="PytHon"

word="python"
new_word=""


for i in range(len(word)):
    if i==0 or i==3:
        cap=word[i].capitalize()
        new_word+=cap
    else:
        lower=word[i].lower()
        new_word+=lower
print(new_word)

    
    
