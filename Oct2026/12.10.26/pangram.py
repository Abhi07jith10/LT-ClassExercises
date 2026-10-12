#a pangram is a sentence,phrase or word that uses every
#letter of a given alphabet at least once

sentence="the quick brown fox jumps over the lazy dog"


alphabets="abcdefghijklmnopqrstuvwxyz"

for i in alphabets:
    if i not in sentence:
        print(f"the sentence is not a pangram")
        break
    
else:
        print(f"the sentence is a pangram")
