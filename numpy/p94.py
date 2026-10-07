import numpy as np

arr = np.array([10, 20, 30, 40, 50])

mean = np.mean(arr)

result = arr[arr > mean]

print("Mean:", mean)
print("Above mean:", result)