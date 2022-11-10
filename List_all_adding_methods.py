 #APPEND METHOD:
A=['all','is','good','and']
A.append("proper")
print(A)
""".append() will add item in the last position."""
#therefore Output will be=['all','is','good','and','proper']


#INSERT METHOD:
B=['all','is','good','and']
B.insert(4,'proper')
print(B)
""".insert needs an index in order to add a item but that means it can be used to add an item anywhere."""
#Output will be=['all','is','good','and','proper']

#EXTEND METHOD:
C=['all','is', 'good','and','proper']
c={'this','is','it!'}
v=('is','it?')
C.extend(c)
C.extend(v)
print(C)
""".extend will extend any iterables by their tail but their should be a main attribute that should be a list."""
#therefore Output will be=['all','is','good','and','proper','this','is','it!','is''it?']