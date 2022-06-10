""" Type casting/declarations can be made to manipulate the existing rules and change the characteristics of the existing data types and use them according to the coder's requirements."""
# These are the ways of type casting/declarations:

x=str(8)# The compiler will see this as "8"
y = int(3.99)# The compiler will see this as 3
z = float(3)# The compiler will see this as 3.0
Y= complex(7)# The compiler will see this as (7+0j)

print(x)
print(y)
print(z)
print(Y)

# The type will be their specific type casting.
print(type(x))# <class 'str'>
print(type(y))# <class 'int'>
print(type(z))# <class 'float'>
print(type(Y))# <class 'complex'>