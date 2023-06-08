import numpy as np

# ndarray: Nth dimensional array which is basically a numpy array.

arr = np.array([[10, 20], [30, 40], [50, 60], [10, 20]])# This creates an ndarray using any iterable of python with .array() function of numpy
arr2 = np.array([[20, 30], [60, 90], [100, 50], [30, 10]])
# Performing mathematical operations on an NDArray returns their elements with the math operations performed.
# On the other hand if we perform addition on two python list it concatenates them.

# numpy has an extended list of data types that go beyond python's data types and it is an optional parameter when creating
# an ndarray if not specified it will automatically sense the datatype.
print("arr: \n", arr)
print(arr.dtype) # dtype - int32
print("arr2: \n", arr2)
print("Adding arr and arr2:")
print(arr+arr2)

s = b"Hello"

# a = np.frombuffer(s, dtype="S1")
# .dtype() function is used to specify the datatype of the elements ndarray will have

dt = np.dtype([('age', np.int8)]) # We can also create a custom dtype for our ndarray
a = np.array([(10,), (20,), (30,)], dtype=dt)
print(a.dtype)# [('age', 'i1')]

print(type(a)) # Will return <class 'numpy.ndarray'>
print(np.array2string(a))