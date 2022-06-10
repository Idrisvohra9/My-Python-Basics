# isinstance() is an inbuilt function which tells us whether many things about python
# Return whether an object is an instance of a class or of a subclass thereof.

# A tuple, as in isinstance(x, (A, B, ...)), may be given as the target to check against. This is equivalent to isinstance(x, A) or isinstance(x, B) or ... etc.

isinstance(1, object)
# True
isinstance(list(), object)
# True
isinstance(True, object)
# True
def foo():
    pass

isinstance(foo, object)
# True
# This program tells us that everything in python is an object.