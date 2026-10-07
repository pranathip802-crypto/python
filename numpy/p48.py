import numpy as np

arr = np.array([10, -5, 20, -8, 30, -2])

arr[arr < 0] = 0

print(arr)