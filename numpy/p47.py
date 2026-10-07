import numpy as np

arr = np.array([10, 12, 15, 22, 25, 31, 40])

result = arr[arr % 5 == 0]

print(result)