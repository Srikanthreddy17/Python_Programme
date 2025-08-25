import numpy as np

arr = np.array([1, 2, 3, 4, 5])
total_sum = np.sum(arr)
print("Total Sum:", total_sum)  # Output: Total Sum: 15
mean_value = np.mean(arr)
print("Mean Value:", mean_value)  # Output: Mean Value: 3.0
max_value = np.max(arr)
print("Max Value:", max_value)  # Output: Max Value: 5 
min_value = np.min(arr)
print("Min Value:", min_value)  # Output: Min Value: 1
std_dev = np.std(arr)
print("Standard Deviation:", std_dev)  # Output: Standard Deviation: 1.4142135623730951
median_value = np.median(arr)
print("Median Value:", median_value)  # Output: Median Value: 3.0
var_value = np.var(arr)
print("Variance:", var_value)  # Output: Variance: 2.0