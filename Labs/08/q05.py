#name: ibrahim johar farooqi
#date: 10 october 2024
#lab: 07
#task: 05

import numpy as np
from numpy import random

mat = np.random.choice([2,5,9,10], size=(4,4))

identity_mat = np.eye(4)

result_mat = mat @ identity_mat

odd_num_mat = np.random.choice(np.arange(1,100,2), size=(4,4))

final_mat = result_mat + odd_num_mat
