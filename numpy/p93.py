import numpy as np

arr = np.array([10, 80, 30, 90, 50, 70])

indexes = np.argsort(arr)[-3:][::-1]

values = arr[indexes]

print("Values:", values)
print("Indexes:", indexes)