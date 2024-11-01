#ibrahim johar farooqi
#23k-0074
#bai-3a
#assignment 2
#q04

import numpy as np

arr = np.arange(5,21).reshape(4,4)
arr2 = np.arange(21,37).reshape(4,4)

print("array 1:\n", arr)
print("\narray 2:\n", arr2)

print("\nafter element-wise addition:\n")
print(arr+arr2)

print("\nafter element-wise subtraction:\n")
print(arr2-arr)

print("\nafter element-wise multiplication:\n")
print(arr*arr2)

print("\nafter element-wise division:\n")
print(arr2/arr)

