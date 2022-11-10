# Tuple is ordered, unchangable, and allows duplicate values.
# Although it is unchangable we can still convert it to list and add or remove items from it and then convert it back to tuple. 
t=("lion","tiger","cheetah","leapord")
# .count()
# count function returns the number of items the item is there in the tuple
print(t.count("lion"))

# .index()
# index function returns the index of the item in the tuple
print(t.index("tiger"))


