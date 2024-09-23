import pandas as pd

#creating panda series
myIndex = ["usa", "canada", "mexico"]

mydata = [1776, 1867, 1821]

myser = pd.Series(index = myIndex, data = mydata)

print(myser)

#print(myser[0])
#print(myser["usa"])

#creating series from a dictionary
ages = {"sam":5, "frank":10, "spike":7}

agesSeries = pd.Series(ages)

print(agesSeries)

