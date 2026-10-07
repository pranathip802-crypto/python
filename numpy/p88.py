import numpy as np

arr = np.array([10, 20, 10, 30, 20, 40, 50, 30])

unique, counts = np.unique(arr, return_counts=True)

duplicates = unique[counts > 1]

print(duplicates)