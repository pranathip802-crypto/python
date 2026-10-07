import numpy as np

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("Original shape:", arr.shape)

result = arr.T

print("Transpose:")
print(result)

print("Transpose shape:", result.shape)