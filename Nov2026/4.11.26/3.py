#using a lambda
#input>> "python is a programming language"
#op  [6,2,1,11,9]

result=lambda text:[len(i) for i in text.split()]
print(result(text="python is a programming language"))