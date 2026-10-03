
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""## Importing the dataset"""
dataset_path = Path(__file__).resolve().parent / "Salary_Data.csv"
dataset = pd.read_csv(dataset_path)

X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values
"""## Splitting the dataset into the Training set and Test set"""
from sklearn.model_selection import train_test_split
X_train , X_test , y_train , y_test = train_test_split(X,y,test_size = 1/3 ,
random_state = 0)
print(X_train)
print (" ")
print (y_train)
print (" ")
print(X_test)
print (" ")
print (y_test)
print (" ")
""" Training the Simple Linear Regression model on the Training set"""
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,y_train)
print(X_train)
print (" ")
print (y_train)
print (" ")
print(X_test)
print (" ")
print (y_test)
""" Predicting the Test set results"""
# X_test = np.array([X_test])
# print(X_test)
y_pred = regressor.predict(X_test)
"""## Visualising the Training set results"""
plt.scatter(X_train,y_train,color='r')
plt.plot(X_train , regressor.predict(X_train),color='b')
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()


""" Visualising the Test set results"""
plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary vs Experience (Test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()
""" Visualizing Test Results by using X_test and y_pred in plt.plot"""
plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_test, y_pred, color = 'blue')
plt.title('Salary vs Experience (Test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()
""" Making a single prediction (for example the salary of an employee with 12
years of experience)"""
single_prediction = regressor.predict([[12]])
print (single_prediction)
coefficient = regressor.coef_
intercept = regressor.intercept_
print ("Coefficient is:",coefficient)
print("Slope/Intercept:" , intercept)
""" Extra Practice"""
manual_prediction = 26816.192244031183 + 9345.94244312*15
print ("Manual prediction by using coefficient and intercept" ,
manual_prediction)
auto_prediction = regressor.predict([[15]])
print("autoprediction:",auto_prediction)