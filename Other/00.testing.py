# Filtering elements without using .filter()


# Creating an instant list with range()

a = list(range(0, 51))

a = list(filter(lambda x: x % 2 == 0, a))
print(a)
