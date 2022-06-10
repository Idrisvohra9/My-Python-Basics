#REMOVE METHOD:
A=['all','is','good','and']
A.remove("and")
print(A)
""".remove() will remove any item specified from the list."""
#therefore Output will be=['all','is','good']
#POP METHOD:
B=['all','is','good','and']
B.pop(3)#or B.pop(-1)
print(B)
B.pop()
print(B)
""".pop() will remove any specified index from the list."""
#.pop() with no specified index will remove the last item from the list.

#Output will be=['all','is','good']

#DEL keyword METHOD:
C=['all','is', 'good','and','proper']
c=['this','is','it!']
del C[1]
del c
print(C)
"""The del keyword can be also used to remove the specified indexed item. If del keyword is used individually with the attribute it will remove the entire list of attribute. """
#therefore Output will be=['all','good','and','proper']
#CLEAR METHOD:
v=['is','it?']
v.clear()
print(v)
""".clear method takes no arguments hence it can be used to remove every items from the list Thus the list becomes empty."""
#therefore the output will be-[]
