# Tuple:
# Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
# Tuples are ordered, Unchangable, and allow duplicate values
# Tuples are surrounded by "()" paranthesis or round brackets.
# Tuple items can be of any data type and can be stored in a single tuple.
# 
huple=("cool","calm","collective","confident","cautious")
nuple=(huple[0:3])
print(nuple)
duple=(huple[-3:-1])
print(duple)
juple=(huple[1:])
print(juple)
cuple=(huple[:-1])
print(cuple)
# We can also access the character inside the tuple to make something new Like:
print(huple[0][0:2]+huple[1][-1]+huple[2][-4:-2]+huple[-1][1])