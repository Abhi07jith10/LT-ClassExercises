#using a lambda
#input>> "python is a programming language"
#op >> {"python":6,"is":2,"a";2,"programming":11,"language":9}

result=lambda text:{i:len(i) for i in text.split()}
print(result(text="python is a programming language"))
