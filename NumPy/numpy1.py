import numpy as np

arr = np.array([[10, 20], [30, 40], [50, 60], [10, 20]])
arr2 = np.array([[20, 30], [60, 90], [100, 50], [30, 10]])
# Performing mathematical operations on an NDArray returns their elements with the math operations performed. On the other hand if we perform addition on two python list it concatenates them.

print("arr: ", arr)
print("arr2: ", arr2)
print("Adding arr and arr2:")
print(arr+arr2)

s = b"Hello"

# a = np.frombuffer(s, dtype="S1")

dt = np.dtype([('age', np.int8)])
a = np.array([(10,), (20,), (30,)], dtype=dt)
print(a["age"])

print(type(a))
# print(np.array2string(a))

dt=np.dtype(np.int32)
print(dt)