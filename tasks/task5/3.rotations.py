#Check Whether Two Strings Are Rotations
# Sample Input 1: "abcd"
# Sample Input 2: "cdab"
# Sample Output: "Rotation"

# Rotating abcd, one step at a time:

# Move a from front to back: bcda
# Move b from front to back: cdab
# Move c from front to back: dabc
# Move d from front to back: abcd (back to the start)

word1="abcd"
word2="cdab"

new_word=word1+word1   #abcdabcd

if len(word1)==len(word2):
        if word2 in new_word:
            print("rotation")
        else:
            print("not rotation")
else:
            print("not rotation")
        
