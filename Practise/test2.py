import pandas as pd

q1 = {'Japan': 80, 'China': 450, 'India':200, 'USA': 250}
q2 = {'Brazil': 100, 'China': 500, 'India': 210, 'USA': 260}

#convert into panda series
sales_Q1 = pd.Series(q1)
sales_Q2 = pd.Series(q2)

print(sales_Q1+sales_Q2)
