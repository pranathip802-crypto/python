import numpy as np

arr = np.array([10, 25, 40, 60, 80, 90])

result = arr[(arr >= 20) & (arr <= 80)]

print(result)