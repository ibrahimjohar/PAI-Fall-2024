#name: ibrahim johar farooqi
#date: 10 october 2024
#lab: 07
#task: 06

import numpy as np

matrix5x3 = np.random.randint(0, 20, (5,3))
matrix3x2 = np.random.randint(0, 20, (3,2))

result = np.matmul(matrix5x3, matrix3x2)

print(result)
