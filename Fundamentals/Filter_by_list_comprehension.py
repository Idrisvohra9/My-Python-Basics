#List comprehension can filter the list as per the coder's wants without using for statements with a condition.
#So list filter without comprehension:
Reptile_animals=["Anaconda","Python","Cobra"]
Empty=[]
for x in Reptile_animals:
  if 'a' in x:
    Empty.extend(x) #Append can also be used.
    print(x)
    #it will print out the list units that contain "a" in the animal list i.e. 'Anaconda, and Cobra'.
#With the use of list comprehension:
Aquatic_animals=["Squid","Jellyfish","Turtle"]
Empty=[x for x in Aquatic_animals if "l" in x]
print(Empty)
