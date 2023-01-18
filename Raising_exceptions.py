<<<<<<< HEAD
n=input("Enter something: ")
try:
    if int(n)<0:
        raise Exception("Value less than zero is not allowed.")
except:
    if type(n) is str:
=======
n=input("Enter something: ")
try:
    if int(n)<0:
        raise Exception("Value less than zero is not allowed.")
except:
    if type(n) is str:
>>>>>>> 66ba5faed76c21bba0a6cb181bc8a77bae565f4f
        raise Exception("Enter a int value.")