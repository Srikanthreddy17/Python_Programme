import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
# Accessing elements using positive indexing
print(arr[0, 0])  # Output: 1
# Accessing elements using negative indexing
print(arr[-1, -1])  # Output: 9
# Slicing the array
print(arr[0:2, 1:3])  # Output: [[2 3] [5 6]]
#print 2 from frist row and 9 from last row
print(arr[0, 1], arr[-1, -1])  # Output: