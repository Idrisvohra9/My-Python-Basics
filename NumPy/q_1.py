import numpy as np

a = np.arange(1,100)

n = a[(a % 3 ==0) | (a % 5 == 0)]
print(n)
print("Sum : ",n.sum())