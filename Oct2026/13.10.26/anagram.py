word1="listen"
word2="silent"

word1,word2=word1.lower(),word2.lower()

if len(word1)==len(word2):
    for i in range(len(word1)):
        if word1.count(word1[i])!=word2.count(word1[i]):
            print("Not anagram")
            break
    else:
        print("Anagram")

else:
    print("Not anagram")
