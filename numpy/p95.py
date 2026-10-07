import numpy as np

arr = np.array([10, np.nan, 20, np.nan, 30])

missing = np.isnan(arr)

percentage = np.sum(missing) / arr.size * 100

print(percentage)