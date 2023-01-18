s={"Lion","Tiger","Cheetah"} #This is a set.
print("Lion" in s)
# The output will be True because it checks for "Lion" in s. and it contains Lion that means the statement is true.
# Similarly this will return False:
print("Lio" in s)
print("\r") # This is just for a new line.

# looping through every item in a set:
for x in s:
    print(x)
# Output:
# Tiger
# Lion
# Cheetah

# Notes:
# Set is one of the four data types of python. There are list, tuple, dictionary and set. Set is unordered, unindexed and unchangable and do not allow duplicate items. set items are unchangable* but we can remove and add items in it.
# Set can contain any data type such as string, int, boolean.
sset={True, False, "hello",123,("Idris","vohra")}
for x in sset:
    print(x)
# Add items in set:
s.add()