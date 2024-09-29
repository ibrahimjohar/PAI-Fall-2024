#name: ibrahim johar farooqi
#date: 25 september 2024
#lab: 06
#task: 6

import pandas as pd

data = pd.read_csv('alcohol.csv')

alcohol_record_1985 = data[data['Year'] == 1987]

print(alcohol_record_1985)

print("\n")

alcohol_record_1986 = data[data['Year'] == 1986]

print(alcohol_record_1986)

