#name: ibrahim johar farooqi
#date: 02 october 2024
#lab: 07
#task: 1

import pandas as pd

df = pd.read_csv("heart-disease.csv")

df = df.rename(columns={"sex" : "gender"})

print(df)

df['gender'] = df['gender'].replace({1: 'male', 0: 'female'})

print(df)
print("\nchol:")
print("median: ", df['chol'].median())
print("mean: ", df['chol'].mean())
print("max: ", df['chol'].max())
print("\nrestecg, chol, oldpeak:")
print("median: ", df[['restecg', 'chol', 'oldpeak']].median())
print("mean: ", df[['restecg', 'chol', 'oldpeak']].mean())
print("max: ", df[['restecg', 'chol', 'oldpeak']].max())
