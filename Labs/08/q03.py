#name: ibrahim johar farooqi
#date: 10 october 2024
#lab: 07
#task: 03

import numpy as np

identity_mat = np.eye(3)
even_arr = np.arange(2, 20, 2).reshape(3,3)

even_arr = 4 * even_arr

result_arr = even_arr * identity_mat

print(result_arr)
