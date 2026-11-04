while True:

    filename=input("enter the file name:")
    try:
        file_1=open(filename,"r")
        result=file_1.read()
        print(result)
        break
    except FileNotFoundError:
        print("File is not found")
print("Thank you")

