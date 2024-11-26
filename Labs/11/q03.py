#name: ibrahim johar farooqi
#date: 13 november 2024
#lab: 11
#task: 03

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, KFold
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

df = pd.read_csv('dermatology.csv')
df = df.dropna()

X = df.values[:, :35]
y = df.values[:, 35]

kf = KFold(10, shuffle=True, random_state=727)

for i, (train_index, test_index) in enumerate(kf.split(X)):
    knn = KNeighborsClassifier(n_neighbors=3)
    knn.fit(X[train_index], y[train_index])
    predictions = knn.predict(X[test_index])
    print(f'Iteration {i+1}:\nConfusion Matrix')
    print(confusion_matrix(y[test_index], predictions))
  
