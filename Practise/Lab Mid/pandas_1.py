import pandas as pd
#dataframes
data = {'Name': ['tom', 'jack', 'steve', 'ricky'], 'Age': [28, 34, 29, 42]}
data = pd.DataFrame(data) #creating a dataframe
print(data.shape) #shape - gives dimensions
print(data)

print("\n")
#series
data = {'Name': ['tom', 'jack', 'steve', 'ricky'], 'Age': [28, 34, 29, 42], 'Roll No.': [12, 19, 23, 9]}
data = pd.Series(data) #creating series
print(data.shape) #shape - gives dimensions
print(data)

xls = pd.ExcelFile('testXLS.xlsx')
df1 = pd.read_excel(xls, 'Sheet1')
df2 = pd.read_excel(xls, 'Sheet2')

print(df1)
print("\n")
print(df2)

