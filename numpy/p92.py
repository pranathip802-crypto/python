import numpy as np

arr = np.array([
    [10, 50, 30],
    [20, 60, 40],
    [30, 70, 50]
])

column_avg = np.mean(arr, axis=0)

result = np.argmin(column_avg)

print("Column index:", result)
print("Lowest average:", column_avg[result])