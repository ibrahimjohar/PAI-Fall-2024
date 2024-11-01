#ibrahim johar farooqi
#23k-0074
#bai-3a
#assignment 2
#q10

import numpy as np

def normalize(arr):
    mean = np.mean(arr)
    std_dev = np.std(arr)
    normalized_arr = (arr - mean) / std_dev
    return normalized_arr

arr = np.array([10, 20, 30, 40, 50])
normalized_arr = normalize(arr)

print("original array:", arr)
print("normalized array:", normalized_arr)
