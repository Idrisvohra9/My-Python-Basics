# map() is a function that iters through the items of iterables(list, tuple) and performs a specified function on them.

# it takes two arguments :1st a function and 2nd an iterable
# code 1: to make the INT in the list to Float.
int_l=[2,3,4,5,6]
float_l= list(map(float,int_l))

print(float_l)
"""
Output:
[2.0, 3.0, 4.0, 5.0, 6.0]
"""

# code 2: To make the string of numbers in the tuple to int.
str_t=("2","3","4","5","6")
int_t= tuple(map(int,str_t))

print(int_t)
"""
Output:
(2, 3, 4, 5, 6)
"""


# Code 3: 
