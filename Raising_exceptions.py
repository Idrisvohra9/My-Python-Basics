n=input("Enter something: ")
try:
    if int(n)<0:
        raise Exception("Value less than zero is not allowed.")
except:
    if type(n) is str:
        raise Exception("Enter a int value.")