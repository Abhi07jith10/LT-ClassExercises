#get a list of 5 numbers and ask the user to enter the index value
#and return the element and also handle the exception.

list=[1,2,3,4,5,6]
while True:
    try:
        index=int(input("enter the index : "))
        result=list[index]
        print(result)
        break
    except ValueError:
        print("Valueerror")
    except IndexError:
        print("index error or index out of range")
    except Exception:   #if in case any other exception comes along
        print("somethng went wrong")

    finally:     #block used to execute the code whether exception occurs or not

        print("Thank you")