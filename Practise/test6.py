import pandas as pd

#merging

registrations = pd.DataFrame({'reg_id': [1,2,3,4], 'name': ['andrew', 'bobo', 'claire', 'david']})

logins = pd.DataFrame({'log_id': [1,2,3,4], 'name':['xavier', 'andrew', 'yoldana', 'bobo']})

print("registration table:")
print(registrations)
print("login id table:")
print(logins)

#inner join
#match up where key is present in both tables, no NaNs due to the join

print("\ninner join")
print(pd.merge(registrations, logins, how='inner', on='name'))

#to check if data is missing in the table read from csv, use **df.isnull()** function
#to not see the the NaNs(empty vals), use the **df.dropna()** function

#to fill the NaNs with a value, use the **df.fillna("insert val here")**

