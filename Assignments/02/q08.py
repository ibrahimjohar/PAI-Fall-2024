#ibrahim johar farooqi
#23k-0074
#bai-3a
#assignment 2
#q08

import numpy as np

a = np.array([[5, 7, 3],
              [6, 2, 8],
              [4, 9, 1]])
b = np.array([2, 5, 7])

solution = np.linalg.solve(a, b)

print("array a: \n", a)
print("array b:\n", b)

print("sols (x, y, z):", solution)