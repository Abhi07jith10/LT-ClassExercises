list=["madam","apple","python","level","radar"]

for i in list.copy():
    
        if i!=i[::-1]:
            list.remove(i)

print(list)
