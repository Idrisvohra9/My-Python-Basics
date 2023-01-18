<<<<<<< HEAD
list1=[7,9.8,'a',"name"]
print(len(list1))
list2=list1.copy() #here if i change in copied list it don't reflect on original list
print(list2)

print(list1.index(7))

print(list1.count(7))

list2=[4,2,3]
list2.reverse()
print(list2)

print(sorted(list2)) #it does not sort the original list it sorts the copy of the original list
list2.sort()  #it sorts the original list
print(list2)

list2.sort(reverse=True)
print(list2)

list2.clear() #it gives us empty list
print(list2)

list3=[78,89,56,49,48,47]
print(max(list3))
print(min(list3))
print(sum(list3))

del list3[2] #delete particular element
print(list3)
del list3[1:3] #also delete elements
print(list3)
lst1=[]                      #Enter the values from user
for i in range(4):
    lst1.append(input("Enter the value:"))
=======
list1=[7,9.8,'a',"name"]
print(len(list1))
list2=list1.copy() #here if i change in copied list it don't reflect on original list
print(list2)

print(list1.index(7))

print(list1.count(7))

list2=[4,2,3]
list2.reverse()
print(list2)

print(sorted(list2)) #it does not sort the original list it sorts the copy of the original list
list2.sort()  #it sorts the original list
print(list2)

list2.sort(reverse=True)
print(list2)

list2.clear() #it gives us empty list
print(list2)

list3=[78,89,56,49,48,47]
print(max(list3))
print(min(list3))
print(sum(list3))

del list3[2] #delete particular element
print(list3)
del list3[1:3] #also delete elements
print(list3)
lst1=[]                      #Enter the values from user
for i in range(4):
    lst1.append(input("Enter the value:"))
>>>>>>> 66ba5faed76c21bba0a6cb181bc8a77bae565f4f
print(lst1)