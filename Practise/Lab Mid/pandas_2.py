import pandas as pd
#dataframes
data = {'Name': ['tom', 'jack', 'steve', 'ricky'], 'Age': [28, 34, 29, 42]}
data = pd.DataFrame(data) #creating a dataframe
print(data.head())
print("\n")

#adding row
new_row = {'Name': "bill", 'Age': 25}
new_index = len(data)
data.loc[new_index] = new_row
print(data)
print("\n")

#adding col
data.loc[:, 'City'] = ['NY', 'LA', 'SF', 'Miami', 'CF']
print(data)
print("\n")

#dropping a row
data = data.drop(index=4)
print(data)
print("\n")

#dropping a col
data = data.drop(columns='City')
print(data)
print("\n")

#data.loc[:, 'City'] = ['NY', 'LA', 'SF', 'Miami', 'CF']
data = data.drop('Age', axis='columns')
print(data)
print("\n")

data.loc[:, 'Age'] = [28, 34, 29, 42]
data.loc[:, 'City'] = ['NY', 'LA', 'SF', 'Miami']
print(data)
print("\n")

#concatenating rows of two csv files/two dataframes
#result = pd.concat([data, data1], ignore_index = True)
#print(result)

#extracting particlar column
print(data[['Age', 'City']])
print("\n")

#iloc accesses rows and cols by indexes
print(data)
print("\n")
print(data.iloc[1][2])
print("\n")

print(data.iloc[0:2, 0:1]) #iloc[start row:end row, start col:end col]
print("\n")

#changing index
print(data)
print("\n")
new_data = data.set_index('Name')
print(new_data)
print("\n")

#using loc
print("jack's info:\n", new_data.loc['jack'])
print("\n")

#filter viewing using loc
print("data of people with age greater than 28")
print(data.loc[data['Age'] > 28])
print("\n")

#sorting data
data.sort_values('Age', inplace=True)
print(data)
print("\n")

#changing a value at a particular position
print("data.at[0, 'Age'] = " , data.at[0, 'Age'])
data.at[0, 'Age'] = 12
print("\n", data)
print("\n")

#dropping cols with all null vals
data.loc[:, 'NA-COL'] = [None, None, None, None]
print(data)
data = data.dropna(axis=1, how='all') #axis=0 or axis='index' removes all rows with NULL vals
print("\n", data)
print("\n")

#replacing yes and no in a col with 1  & 0
data.loc[:, 'Old?'] = ['no', 'no', 'yes', 'yes']
print(data)
data['Old?'].replace({'no' : 0, 'yes' : 1}, inplace=True)
print("\n", data)



