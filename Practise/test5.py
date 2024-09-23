import pandas as pd

#directly glue together dataframes

data_one = {'A': ['A0', 'A1', 'A2', 'A3'], 'B': ['B0', 'B1', 'B2', 'B3']}

data_two = {'C': ['C0', 'C1', 'C2', 'C3'], 'D': ['D0', 'D1', 'D2', 'D3']}

one = pd.DataFrame(data_one)
two = pd.DataFrame(data_two)

print(one)
print("\n")
print(two)
print("\n")

axis0 = pd.concat([one,two],axis=0) #concat along rows, axis=0
print(axis0)

print("\n")

axis1 = pd.concat([one, two], axis=1) #concat along cols, axis=1
print(axis1)

two.columns = one.columns #concat, where the columns match up below eachother
print(pd.concat([one,two]))


