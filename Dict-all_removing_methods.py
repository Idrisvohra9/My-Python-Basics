onedict={
    "fruit" : "apple",
    "colour" : "red",
    "type" : "seedy",
    "Minerals" : "Fiber, vitamin-c"
}
# 1. .pop()
# .pop() will remove the specified item name from the dictionary.
onedict.pop("Minerals")
print(onedict)
# Output : {'fruit': 'apple', 'colour': 'red', 'type': 'seedy'}

# 2. .popitem() 
# .popitem() will remove the last item from the dictionary.
onedict.popitem()
print(onedict)
# Output : {'fruit': 'apple', 'colour': 'red'}

# 3. del keyword
# del keyword removes a specified item from the dictionary and using only del keyword makes the dictionary void and that will raise an error if printed.
del onedict["colour"]
print(onedict)
# output : {'fruit': 'apple'}

# 4. .clear()
# .clear() will empty the dictionary entirely.
onedict.clear()
print(onedict)
# Output : {}