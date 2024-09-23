import pandas as pd

#grouping

#a groupby() operation allows us to examine data on a per category basis

df = pd.read_csv("results.csv")

print(df.groupby('year', 'event').mean())
