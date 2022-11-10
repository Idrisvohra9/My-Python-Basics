Animals=["Lion","Tiger","Deer","Zebra","Wolf","Leopard"]

# $ This will only print the elements of the list that contains "e":
print([x for x in Animals if "e" in x])
#output=["Tiger","Deer","Zebra","Wolf","Leopard"]

# $ This will only print the elements of the list that does't contain "e":
print([x for x in Animals if "e" not in x])
#output["Lion","Wolf"]

# $ This will only print the elements of the list that are not "Deer":
print([x for x in Animals if "Deer" != x])
#output=["Lion","Tiger","Zebra","Wolf","Leopard"]

# $ This will only print the elements of the list that are not "Zebra":
print([x for x in Animals if "Zebra" != x])
#output=["Lion","Tiger","Deer","Wolf","Leopard"]

# $ This will transform the string text in the list to uppercase:
print([x.upper() for x in Animals]) # # The same cane be done in lowercase with .lower()
#Output=["LION","TIGER","DEER","ZEBRA","WOLF","LEOPARD"]

# $ Sorting List in ascending order:
Animals.sort()
print(Animals)
#output=["Deer","Leopard","Lion","Tiger","Wolf","Zebra"]

# $ Sorting list in descending order:
Animals.sort(reverse=True)
print(Animals)
#output=["Zebra","Wolf","Tiger","Lion","Leopard","Deer"]