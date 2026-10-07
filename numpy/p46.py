import numpy as np

arr = np.array([10, 15, 22, 31, 40, 55])

result = np.sum(arr % 2 == 0)

print(result)