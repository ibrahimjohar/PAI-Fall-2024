import pandas as pd

data = pd.read_csv('heart.csv')
print("data.head():")
print( data.head(3) ) #default empry parameters give first 5 rows
print("\ndata.tail():")
print( data.tail(3) )

#changing name of all columns
data.columns = ['age', 'sex', 'chest_pain_type', 'resting_bp', 'cholestral', 'fasting_blood_sugar', 'resting_ecg', 'max_heart_rate_achieved', 'exercise_induced_angina', 'st_depression', 'st_slope', 'num_major_vessels', 'thalassema', 'target']
print(data)

#changing name of specific columns
data = data.rename(columns = {'sex': 'gender', 'chest_pain_type': 'cpt'})
print(data.head())

#for information about the csv file, use 'describe'
print(data.describe())

#insert column using 'insert(loc, column, list)'
data = data.head(10)
names = ['Ali', 'Salman', 'Sohail', 'Mohsin', 'Waqas', 'Zeshan', 'Babar', 'John', 'Elon', 'Michael']
data.insert(0, 'name', names)
print(data.head(10))

#make new dataframe
ndata = data.head(5) #only 5 rows of info
ndata = data[['age', 'gender', 'cpt', 'target']] #select specified cols
print(ndata)

#dropping column
ndata.drop(labels=['target'], axis=1, inplace=True)
print(ndata.head())



