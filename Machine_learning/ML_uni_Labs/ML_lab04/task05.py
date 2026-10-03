from pathlib import Path
import math

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

"""## Load local dataset"""
dataset_path = Path(__file__).resolve().parent / "insurance_data.csv"
df = pd.read_csv(dataset_path)

print(df.head())

"""## Scatter plot"""
plt.scatter(df['age'], df['bought_insurance'], marker='+', color='red')
plt.xlabel('Age')
plt.ylabel('Bought Insurance')
plt.title('Insurance purchase by age')
plt.show()

"""## Train Test Split"""
X = df[['age']]
y = df['bought_insurance']
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    train_size=0.8,
    random_state=42,
)

"""## Logistic Regression model"""
model = LogisticRegression()
model.fit(X_train, y_train)

"""## Prediction"""
y_pred = model.predict(X_test)
print(np.column_stack((y_pred, y_test.to_numpy())))
print('Model accuracy:', model.score(X_test, y_test))
print('Coefficient:', model.coef_)
print('Intercept:', model.intercept_)

"""## Sigmoid function"""
def sigmoid(x):
    return 1 / (1 + math.exp(-x))


def prediction_function(age):
    z = model.coef_[0][0] * age + model.intercept_[0]
    return sigmoid(z)


for age in [35, 43]:
    p = prediction_function(age)
    print(f'Probability age={age} buys insurance: {p:.4f}')
    if p < 0.5:
        print('This person is less likely to buy insurance.')
    else:
        print('This person is more likely to buy insurance.')
