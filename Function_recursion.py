def factorial_iter(n): # n is a factorial number placeholder or parameter.
    m=1
    for x in range(n):
        m = m*(x+1)
    return m
print(factorial_iter(9)) # this will be read as n.
# Output: 362880


def factorial_recursive(n):
    if n == 0 or n == 1: # This is mandatory! or else the program wouldn't be completed.
        return 1 # there should be a base condition whle using recursion or else the program would go on infinitely and would cause a stack overflow.
    else:
        return n* factorial_recursive(n-1)
print(factorial_recursive(9))
# Output: 362880