#Default arguments:
def arg1(a,b=4):
    # In this function the arguments that are passed b is given 4 by default and hence it will return according to assuming the value of b=4. Therefore we can say b is the default argument.
    sum=a+b
    return sum #The reason why return is used is because the function can return a value when called and be printed with added benifits of text editing. 
print("The sum = {}".format(arg1(5))) # if b is given as an default argument then this will be the value of a.
#output=9
    #We can also give an value to b even though it is a default argument when the function is being called the default arguments gets overwrite by the calling argument. Therefore we can also do this:
print("The sum = {}".format(arg1(5,10))) # in this a=5 and b will be overwrite as the calling argument 10.
# Output=15
# Keyword argument:
# Keyword arguments means that when you call the function you add the particular parameters values during the call. you add the values as per the argument variable name.
# for example:
def arg2(a,b,c):
    return (a+b+c)/3 #This averages the values passed.
print("The averages = {}".format(arg2(b=3,c=9,a=10)))
# When you use keyword arguments you do not have to pass the values according to the order you can just pass it in any order you like.
# Positional arguments:
# Positional arguments are those in which we call the function with values by keeping in mind the order in which the parameters are defined.
# for example:
print("The averages = {}".format(arg2(10,3,9))) #In this according to positional arguments a=10 b=3 and c=9.

# Points to remember:
# 1. default arguments should follow non default arguments. Or otherwise error such as:
#Output: SyntaxError: non-default argument follows default argument |will appear.
# 2. keyword arguments should follow positional arguments. Or otherwise error such as:
#Output: SyntaxError: positional argument follows keyword argument |will appear.
# 3. All the keyword arguments passed must match all of the arguments accepted by the function and their order is not important.
# print("The averages = {}".format(arg2(10,b1=3,c=9))) #This will generate an error:
#Output: TypeError: arg2() got an unexpected keyword argument 'b1'
# 4. No argument should receive a value more than once.
# print (arg2(a=10,b=5,b=10,c=12))
#Output: SyntaxError: keyword argument repeated : b
# 5. Default arguments are optional arguments.

# Arbituary arguments:
# Functions in which the number of arguments are not specified during the function definition  the "*" (asteric) symbol is used with a variable parameter while defining the function are known as arbituary arguments. This means that you can pass any number of arguments in the function when called.
# There are 2 types of arbituary arguments
# a) Arbituary positional arguments:
def add(*n):
    sum=0
    for i in n:
        sum=sum+i
    return sum
print(add(56,44))
# Arbituary keyword arguments:
# For arbitrary positional argument, a double asterisk (**) is placed before a parameter in a function which can hold keyword variable-length arguments.
def info(**a):
