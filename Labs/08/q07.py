#name: ibrahim johar farooqi
#date: 10 october 2024
#lab: 07
#task: 07

import numpy as np

arr = np.random.randint(0, 1000, 1000)

average = np.mean(arr)
variance = np.var(arr)
std_deviation = np.std(arr)

results = f"average: {average}\nvariance: {variance}\nstandard Deviation: {std_deviation}"

filename = 'stats_info.txt'
with open(filename, 'w') as file:
    file.write(results)

print(f"results saved/written to {filename}")
