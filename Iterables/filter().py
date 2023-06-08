# filter() is a function that iters through the items of iterables(list, tuple) and returns only the value/s that are passed on to the filter's first argument.

# Majorly lambda functions are implemented in a filter
# Syntax = filter(func(), iterable)

# Problem:

# filter out only the even numbers from 0 to 50
# Execution:

# Creating an instant list with range()

a = list(range(0,51))

a = list(filter(lambda x: x %2 == 0, a))
print(a)
# // Output: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]