#name: ibrahim johar farooqi
#date: 25 september 2024
#lab: 06
#task: 2

import pandas as pd

data = pd.read_csv("movie_dataset.csv")

print(data["runtime"].sort_values(ascending=False))