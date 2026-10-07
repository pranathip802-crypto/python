import numpy as np

arr = np.array([
    [30, 10, 20],
    [60, 40, 50],
    [90, 70, 80]
])

result = np.sort(arr, axis=1)

print(result)