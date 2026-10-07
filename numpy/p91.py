import numpy as np

arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [5, 10, 15]
])

row_sums = np.sum(arr, axis=1)

result = np.argmax(row_sums)

print("Row index:", result)
print("Highest sum:", row_sums[result])