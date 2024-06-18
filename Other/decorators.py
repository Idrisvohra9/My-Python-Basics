# Decorator are a special syntax in python that start with the '@' symbol when calling them. They are used on top of the function. And a decorator itself is a function.
# ? What do they do?
# -> Without changing the code they provide additional functionalities to the function they are decorated on or reside on.

# ? How they do it?
# -> Functions are objects in python for that reason they can be passed to the other functions as a parameter. And inside these functions they can be called
import time
# Below code demonstrates how this works:

def f1():
    print("Function f1 called.")

# This function takes a function as an argument and calls it


def f2(f: object):
    f()


f2(f1)
print()

# Wrapper function with added functionalities for functions passed in:


def returnsWrapper(f):
    def wrapper():
        print("Started")
        f()
        print("Finished")
    return wrapper


print()
# The function above returns a wrapper function so we have to call the function 'returnsWrapper' again. This way:

returnsWrapper(f1)()

print()
# The strange syntax here is the reason for the decorators to exist
# This is what we can do to achieve the same thing using decorators:


@returnsWrapper
def f3():
    print("Hello")


f3()
print()
# Decorators are the functions that take a function as an argument and return another function with additional functionalities so we need to call the function with it's name only instead of the function it is decorated with.

# ? How to handle Decorator on a function with infinite arguments and keyword arguments


def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Started")
        func(*args, **kwargs)
        print("Finished")
    return wrapper


@my_decorator
def myfunc1(a, b, c):
    print(a, b, c)


myfunc1(10, 20, 30)
print()

# Using decorators with Functions that return a value


def static_return(f):
    def wrapper(*args, **kwargs):
        # Here we are storing the return value of the function
        val = f(*args, **kwargs)
        print("Function: ", f)
        print("Argument/s: ", args)
        # And then returning it.
        return val
    return wrapper


@static_return
def add(a: list):
    return sum(a)


print(add([10, 20, 30]))
print()

# Real life examples of the decorators use case:

def calculate_time(f):
  def wrapper(*args):
    start_time = time.time()
    res = f()
    end_time = time.time()
    print("Time taken:", int(end_time - start_time), "seconds")
    return res
  return wrapper

@calculate_time
def five_seconds_wait():
  time.sleep(5)
  return "Completed"
  
print(five_seconds_wait())