<<<<<<< HEAD

#$ update tuples:-
# # the values stored in the tuple cannot be changed but there are methods to update and add new values/elements even in tuples

# ! 1st-> TO CONVERT IT INTO LIST AND APPEND NEW VARIBLES AND THEN CONVERT IT AGAIN:
huple = ("cool", "calm", "collective", "confident")
hulist = list(huple)
hulist.append("cautious")
print(tuple(hulist))
# # Output: ('cool', 'calm', 'collective', 'confident', 'cautious')

# ?-> you can also use .insert() and .extend() method by doing this.

# # Manipulate/CHANGE ITEMS:
huple = ("cool", "calm", "collective", "confident")
l = list(huple)
l[2] = "creative"
print(tuple(l))
# # Output: ('cool', 'calm', 'creative', 'confident')


# ! 2nd-> ADD TUPLE TO TUPLE OR CONCATANATE TWO TUPLES:
huple = ("cool", "calm", "collective", "confident")
h = ("curious",)
# ?-> comma',' is mandatory.
print(huple + h)
# # Output: ('cool', 'calm', 'collective', 'confident', 'curious')


# #REMOVE TUPLE ITEMS:
huple = ("cool", "calm", "collective", "confident")
t = list(huple)
t.pop(3)
print(tuple(t))
# # Output: ('cool', 'calm', 'collective')

# ?-> you can also use different list item removing methods such as .remove() , del keyword, .
=======
# update tuples:-
# the variables in the tuple cannot be changed but there are methods to update and add new variables even in tuples
# 1st-> TO CONVERT IT INTO LIST AND APPEND NEW VARIBLES AND THEN CONVERT IT AGAIN:
huple = ("cool", "calm", "collective", "confident")
hulist = list(huple)
hulist.append("cautious")
print(tuple(hulist))
# NOTE-> you can also use .insert() and .extend() method by doing this.
# CHANGE ITEMS:
huple = ("cool", "calm", "collective", "confident")
l = list(huple)
l[2] = "creative"
print(l)
# 2nd-> ADD TUPLE TO TUPLE:
huple = ("cool", "calm", "collective", "confident")
h = ("curious",)
print(huple + h)
# NOTE-> comma',' is mandatory.
# REMOVE TUPLE ITEMS:
huple = ("cool", "calm", "collective", "confident")
t = list(huple)
t.pop(3)
print(t)
# NOTE-> you can also use different list item removing methods such as .remove() , del keyword, .
>>>>>>> 66ba5faed76c21bba0a6cb181bc8a77bae565f4f
