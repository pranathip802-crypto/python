import numpy as np

arr = np.array([10, 20, 10, 30, 20, 40, 10])

unique, counts = np.unique(arr, return_counts=True)

for value, count in zip(unique, counts):
    print(value, ":", count)