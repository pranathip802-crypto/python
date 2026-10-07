import numpy as np

arr = np.array([
    [10, 20, 30],
    [40, np.nan, 60],
    [70, 80, 90],
    [np.nan, 20, 30]
])

result = arr[~np.isnan(arr).any(axis=1)]

print(result)