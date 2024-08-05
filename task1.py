# -*- coding: utf-8 -*-
"""task1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Eh3DYLbnYX6I9lTZgE-al3nioe_96K1p
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt


#Loading the dataset
data = pd.read_csv('/content/train.csv')


X = data[['GrLivArea', 'BedroomAbvGr', 'FullBath']]
y = data['SalePrice']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)


#Evaluating the Model
mse = mean_squared_error(y_test, y_pred)
rmse = (mse)**0.5
r2 = r2_score(y_test, y_pred)



print(f'Mean Squared Error: {mse:.2f}')
print(f'Root Mean Squared Error: {rmse:.2f}')
print(f'R-squared: {r2:.2f}')

Mean Squared Error: 2806426667.25
Root Mean Squared Error: 52975.72
R-squared: 0.63

plt.scatter(y_test, y_pred)
plt.xlabel('Actual Prices')
plt.ylabel('Predicted Prices')
plt.title('Actual Prices vs Predicted Prices')
plt.show()