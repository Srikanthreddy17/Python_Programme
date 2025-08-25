import numpy as np

arr = np.arange(24)         # Create an array with 24 elements
print(arr)
arr_4x6 = arr.reshape(4, 6)     # Reshape to 4 rows and 6 columns
print(arr_4x6)
arr_8x3 = arr.reshape(8, 3)     # Reshape to 8 rows and 3 columns
print(arr_8x3)
arr_3x2x4 = arr.reshape(3, 2, 4)    # Reshape to 3 layers, 2 rows, and 4 columns
print(arr_3x2x4)
arr_flattened = arr_4x6.flatten()   # Flatten the 4x6 array to a 1D array
print(arr_flattened)