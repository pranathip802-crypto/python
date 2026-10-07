import numpy as np

arr = np.array([50, 120, 80, 150, 90, 200])

arr[arr > 100] = 100

print(arr)