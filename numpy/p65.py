import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

arr[arr % 2 == 0] = 0

print(arr)