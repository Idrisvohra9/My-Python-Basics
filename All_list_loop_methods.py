<<<<<<< HEAD
#Normal  "for" list loops:
fruitlist=["Orange","Mango","Pineapple"]

for x in fruitlist:
  print(x)


#Method 2 "for" loop with "range" and "len":
fruitlist=["Strawberry","Banana","Apple"]

for i in range(len(fruitlist)):
  print(fruitlist[i])


#Method 3 "While" loops:
fruitlist=["Pears","Grapes","Promegranate"]
x=0
while x<len(fruitlist):
  print(fruitlist[x])
  x+= 1

#Method 4 "list comprehension":
fruitlist=["Jackfruit","Coconut","Dragon fruit"]
[print(x)for x in fruitlist]
=======
#Normal  "for" list loops:
fruitlist=["Orange","Mango","Pineapple"]
for x in fruitlist:
  print(x)
#Method 2 "for" loop with "range" and "len":
fruitlist=["Strawberry","Banana","Apple"]
for i in range(len(fruitlist)):
  print(fruitlist[i])
#Method 3 "While" loops:
fruitlist=["Pears","Grapes","Promegranate"]
x=0
while x<len(fruitlist):
  print(fruitlist[x])
  x+= 1
#Method 4 "list comprehension":
fruitlist=["Jackfruit","Coconut","Dragon fruit"]
[print(x)for x in fruitlist]
>>>>>>> 66ba5faed76c21bba0a6cb181bc8a77bae565f4f
"""These are not all of the methods used for looping but extra methods are being known and experimented on"""