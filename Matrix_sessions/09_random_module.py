import numpy as np

arr1 = np.random.rand(3, 4)  # Generates a 3x4 array of random floats in the range [0.0, 1.0)
print(arr1)

arr2 = np.random.randint(1, 10, (4, 6))  # Generates a 2x3 array of random integers between 1 and 10
print(arr2)

arr3 = np.random.randn(2, 2)  # Generates a 2x2 array of random floats from the standard normal distribution
print(arr3)