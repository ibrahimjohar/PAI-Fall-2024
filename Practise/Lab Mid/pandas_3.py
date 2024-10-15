import pandas as pd

# Sample DataFrames
registrations = pd.DataFrame({'reg_id': [1, 2, 3, 4], 'name': ['Andrew', 'Bobo', 'Claire', 'David']})
logins = pd.DataFrame({'log_id': [1, 2, 3, 4], 'name': ['Xavier', 'Andrew', 'Yolanda', 'Bobo']})

# Merge the two DataFrames based on the 'name' column (inner join)
df = pd.merge(registrations, logins, how='inner', on='name')
print("Merged DataFrame (Inner Join):")
print(df)
print("\n")

#Example using apply() - converting names to uppercase
def to_uppercase(name):
    return name.upper()

#Apply the function to the 'name' column
df['name_upper'] = df['name'].apply(to_uppercase)

print("DataFrame with 'name' column converted to uppercase:")
print(df)
print("\n")

# Group by reg_id as you already did
df1 = registrations.groupby('reg_id')
print("GroupBy Object:")
print(df1)
print("\n")

print(df)
df.loc[:, 'age'] = [12, 25]
print("\n", df)

#using between() function
filteredDF = df['age'].between(10, 20, inclusive='both')
print("\n", filteredDF)
print("\n")

#nlargest() & nsmallest()
print(df.nlargest(2, 'age'))
print("\n")
print(df.nsmallest(2, 'age'))
