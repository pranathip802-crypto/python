import numpy as np

arr = np.array([
    [30, 60, 20],
    [10, 40, 50],
    [90, 70, 80]
])

result = np.sort(arr, axis=0)

print(result)