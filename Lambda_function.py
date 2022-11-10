# Lambda is a keyword to create an anonymous function that is used for its preciseness it accepts n number of arguments and returns an expression.
x= lambda a,b,c: a+b-c
print(x(5,5,10))
# Output: 0
# The power of lambda is better shown when you use them as an anonymous function inside another function.

# Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:

def fun(n):
     return lambda a : a * n
doubler= fun(2)# This becomes the value taken by the function parameter n.
tripler= fun(3)
print(doubler(2))
print(tripler(3))# 2,3 will be taken by the parameter of lambda a.
# therefore the output will be the multiplication of the both arguments= 4  9