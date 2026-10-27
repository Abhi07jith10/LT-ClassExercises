#a pangram is a sentence,phrase or word that uses every
#letter of a given alphabet at least once

sentence="The Quick brown fox jumps over the lazy dog"

alphabets="abcdefghijklmnopqrstuvwxyz"

for i in alphabets:
    if i not in sentence:
        print("the sentence is not pangram")
        break
else:
    print("the sentence is a pangram")