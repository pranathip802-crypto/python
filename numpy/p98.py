import numpy as np

arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

row_mean = np.mean(arr, axis=1)
column_mean = np.mean(arr, axis=0)

print("Row-wise mean:", row_mean)
print("Column-wise mean:", column_mean)