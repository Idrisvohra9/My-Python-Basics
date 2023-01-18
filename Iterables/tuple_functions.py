tup1=(9,10,1.1,'a','b',[5,4],{"id":1234},"shree ram","hanuman")
tup=(12,89,45,(48,55,98),78)
t2=(89,56,23,78,76,25,59,78)
print(len(tup1))
print(max(t2))
print(min(t2))
print(sum(t2))
print(tup1.index('a')) #returns the index of that element
print(t2.count(78)) #counts the object in a tuple
print(sorted(t2)) # take elements in a tuple and return a new sorted list(doesn't sort the tuple itself)
print(sorted(t2,reverse=True))
for i,value in enumerate(t2): #it gives us values with indexing 
    if i%2==0:
        print(i,value)
for i,value in enumerate(t2,1): #here we change default start value
    print(i,value)
