import numpy as np

a = np.array([9,9,9,5,4,2])

counts = np.bincount(a)
print(np.argmax(counts))