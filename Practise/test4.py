import pandas as pd

df = pd.read_csv("results.csv")

#print(df)

print(df.columns)
print("\n")
print(df.index)
print("\n")
print(df.head())
print("\n")
print(df.tail(3))
print("\n")
print(df.info())
print("\n")
print(f"length of df: {len(df)}")
print("\n")
print(df.describe())
print("\n")
print(df.sample(5))
print("\n")
df.head()
print(df.loc[0:3]) #grab rows
print("\n")
print(df.iloc[0:5], [0,2]) #grab columns

