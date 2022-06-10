# An iterable is an object that contains more than one value.

# An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.

# The iterables in python include: STRING, LIST, TUPLE, DICTIONARY, SET, and range() object

# In action:-
string="Idris"
l=[1,2,3,4,5]
t=(1,2,3,4,5)
d={1:"i",2:"d",3:"r",4:"i",5:"s"}
s={1,2,3,4,5}
r=range(1,10)

print(iter(string))
print(iter(l))
print(iter(t))
print(iter(d))
print(iter(s))
print(iter(r))

# The output signifies that these data types are iterable

print()
myit= iter(string)
# Making a iterable of string
# and then printing the values from it with next() function.
for i in range(0,len(string)):
    print(next(myit),end="")

print()
# The same can be done with every other iterables but with dictionary only the key values will be printed out.

# Looping can also be done like this:
for i in string:
    print(i)

# In dictionary:
for keys, values in d.items():
    print(f"{keys} : {values}")

# Creating a iterable object:
# Making a literal class like range:
class IterNumbers:
    def __init__(self,start,stop,step=1):
        self.start = start
        self.stop = stop
        self.step = step
    
    def __iter__(self):
        self.start = self.start
        return self

    def __next__(self):
        if self.start<=self.stop:
            next= self.start
            self.start+=self.step
            return next
        else:
            raise StopIteration

# This is also the same range class but for chars
class IterChar:
    def __init__(self,start_char,stop_char,step=1):
        self.start_char = ord(start_char)
        self.stop_char = ord(stop_char)
        self.step = step

    def __iter__(self):
        self.start_char = self.start_char
        return self

    def __next__(self):
        if self.start_char<=self.stop_char:
            next= self.start_char
            self.start_char+=self.step
            return chr(next)
        else:
            raise StopIteration

# Range class literally
for i in IterNumbers(1,20):
    print(i,end=" ")
# print(iter(Iternumbers()))
print()
# Range class for chars
for a in IterChar('A','Z'):
    print(a,end=' ')