import numpy as np

arr = np.array([10, 20, 30, 40, 50])

mean = np.mean(arr)

arr[arr < mean] = mean

print(arr)