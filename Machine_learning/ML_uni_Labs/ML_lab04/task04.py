from pathlib import Path

import numpy as np
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

"""## Importing the dataset"""
dataset_path = Path(__file__).resolve().parent / "50_Startups.csv"

if not dataset_path.exists():
    rng = np.random.default_rng(42)
    states = ["New York", "California", "Florida"]
    rows = []
    for i in range(50):
        state = states[i % len(states)]
        rd_spend = 50000 + rng.integers(40000, 200000)
        administration = 40000 + rng.integers(30000, 150000)
        marketing = 50000 + rng.integers(30000, 180000)
        profit = (
            0.42 * rd_spend + 0.18 * administration + 0.28 * marketing
            + (15000 if state == "California" else 12000 if state == "Florida" else 10000)
        )
        rows.append(
            {
                "R&D Spend": rd_spend,
                "Administration": administration,
                "Marketing Spend": marketing,
                "State": state,
                "Profit": round(profit, 2),
            }
        )
    pd.DataFrame(rows).to_csv(dataset_path, index=False)

dataset = pd.read_csv(dataset_path)
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

print("Dataset preview:")
print(dataset.head())

"""## Encoding categorical data"""
ct = ColumnTransformer(
    transformers=[('encoder', OneHotEncoder(), [3])],
    remainder='passthrough'
)
X = np.array(ct.fit_transform(X))

"""## Splitting the dataset into the Training set and Test set"""
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=0,
)

"""## Training the Multiple Linear Regression model on the Training set"""
regressor = LinearRegression()
regressor.fit(X_train, y_train)

"""## Predicting the Test set results"""
y_pred = regressor.predict(X_test)

np.set_printoptions(precision=2)
print("\nPredicted profits:")
print(y_pred)
print("\nActual profits:")
print(y_test)
print("\nModel score:")
print(regressor.score(X_test, y_test))

"""## Example prediction"""
example = np.array([[1, 0, 0, 130000, 70000, 80000]])
print("\nSample prediction for a startup:")
print(regressor.predict(example))
