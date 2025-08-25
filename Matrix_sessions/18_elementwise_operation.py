import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
# Element-wise addition
result_add = arr1 + arr2
print("Element-wise addition:", result_add)  # Output: [5 7 9]
# Element-wise subtraction
result_sub = arr1 - arr2
print("Element-wise subtraction:", result_sub)  # Output: [-3 -3 -3]
# Element-wise multiplication
result_mul = arr1 * arr2
print("Element-wise multiplication:", result_mul)  # Output: [4 10 18]
# Element-wise division
result_div = arr1 / arr2
print("Element-wise division:", result_div)  # Output: [0.25 0.4  0.5 ]
# Element-wise exponentiation
result_exp = arr1 ** arr2
print("Element-wise exponentiation:", result_exp)  # Output: [  1  32 729]
#element-wise exponentiation
result_exp2 = np.power(arr1, arr2)