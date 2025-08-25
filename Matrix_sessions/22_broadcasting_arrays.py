import numpy as np

#create a 2D array
arr_2d = np.array([[1, 2, 3], 
                   [4, 5, 6]])

#create a 1D array
arr_1d = np.array([10, 20, 30])

# using Broadcasting
result1 = arr_2d + arr_1d # This will add arr_1d to each row of arr_2d
print("Result of Broadcasting: \n", result1)