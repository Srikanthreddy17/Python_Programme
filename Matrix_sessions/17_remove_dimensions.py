import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr.shape)  # Output: (5,)
arr_new = arr[np.newaxis, : ] # Add a new dimension at the beginning
print(arr_new.shape)  # Output: (1, 5)
print(arr_new)  # Output: [[1 2 3 4 5]]

arr_new_2 = arr[:, np.newaxis]  # Add a new dimension at the end
print(arr_new_2.shape)  # Output: (5, 1)
print(arr_new_2)  # Output: [[1] [2] [3] [4] [5]]