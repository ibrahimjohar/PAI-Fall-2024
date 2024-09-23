import numpy as np
import pandas as pd

#data frames is a table of columns and rows in pandas that we
#can easily restructure and filter

#a group of pandas series objects that share the same index

np.random.seed(101)

mydata = np.random.randint(0, 101, (4,3))

myIndex = ['CA', 'NY', 'AZ', 'TX']

myColumns = ['Jan', 'Feb', 'Mar']

df = pd.DataFrame(data = mydata)

print(df)

df = pd.DataFrame(data = mydata, index = myIndex, columns = myColumns)

print("\n", df)

