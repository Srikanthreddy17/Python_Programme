import numpy as np

arr = np.arange(1, 6, dtype = np.int64)
print(np.sqrt(arr))  # Output: [1.         1.41421356 1.73205081 2.         2.23606798]
print(np.log(arr))  # Output: [0.         0.69314718 1.09861229 1.38629436 1.60943791]
print(np.exp(arr))  # Output: [  2.71828183   7.3890561   20.08553692  54.59815003 148.4131591 ]
print(np.sin(arr))  # Output: [0.84147098 0.90929743 0.14112001 -0.7568025  -0.95892427]
print(np.cos(arr))  # Output: [ 0.54030231 -0.41614684 -0.9899925  -0.65364362  0.28366219]
print(np.tan(arr))  # Output: [ 1.55740772 -2.18503986 -0.14254654  1.15782128 -3.38051501]