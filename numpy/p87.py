import numpy as np

arr = np.array([10, 80, 30, 60, 90, 40, 70])

index = np.argpartition(arr, -3)[-3:]

result = arr[index]

print(result)