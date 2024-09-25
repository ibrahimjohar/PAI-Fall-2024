#name: ibrahim johar farooqi
#date: 25 september 2024
#lab: 06
#task: 1

import pandas as pd

data = pd.read_csv("movie_dataset.csv")
print(data[(data['revenue'] > 2000000) & (data['budget'] < 1000000)])
