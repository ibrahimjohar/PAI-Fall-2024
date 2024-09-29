#name: ibrahim johar farooqi
#date: 25 september 2024
#lab: 06
#task: 7

import pandas as pd

df = pd.read_excel('employee.xlsx')

filtered_employees = df[df['Year'] == 2020]

print(filtered_employees)
