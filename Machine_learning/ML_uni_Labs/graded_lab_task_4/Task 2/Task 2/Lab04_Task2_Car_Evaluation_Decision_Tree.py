"""Lab 04 - Decision Tree: Predict Car Acceptability.

Place car.data in the same folder as this script before running it.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier, plot_tree


DATA_FILE = Path(__file__).with_name("car.data")
COLUMN_NAMES = [
    "buying",
    "maint",
    "doors",
    "persons",
    "lug_boot",
    "safety",
    "class",
]


def main():
    # Step 2: Load the dataset
    if not DATA_FILE.exists():
        raise FileNotFoundError(
            f"Could not find {DATA_FILE.name}. Place it in {DATA_FILE.parent}."
        )

    df = pd.read_csv(
        DATA_FILE,
        header=None,
        names=COLUMN_NAMES,
    )
    print(df.head())

    # Step 3: Explore the data
    print("Shape:", df.shape)
    df.info()
    print("\nMissing values per column:")
    print(df.isnull().sum())

    print("\nCars in each class:")
    print(df["class"].value_counts())
    df["class"].value_counts().plot(
        kind="bar",
        figsize=(6, 4),
        title="Class distribution",
    )
    plt.show()

    # Step 4: Encode all columns
    df_encoded = df.copy()
    encoders = {}

    for column in df_encoded.columns:
        encoders[column] = LabelEncoder()
        df_encoded[column] = encoders[column].fit_transform(
            df_encoded[column]
        )

    print("\nEncoded data:")
    print(df_encoded.head())

    print("\nCategory mappings:")
    for column, encoder in encoders.items():
        mapping = dict(
            zip(
                encoder.classes_,
                encoder.transform(encoder.classes_),
            )
        )
        print(column, "->", mapping)

    # Step 5: Separate features and target, then split the data
    X = df_encoded.drop("class", axis="columns")
    y = df_encoded["class"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.3,
        random_state=1,
        stratify=y,
    )

    print("\nTraining samples:", X_train.shape[0])
    print("Testing samples: ", X_test.shape[0])

    # Step 6: Build and train the unpruned decision tree
    model = DecisionTreeClassifier(random_state=1)
    model.fit(X_train, y_train)

    # Step 7: Evaluate the unpruned model
    y_pred = model.predict(X_test)
    print("\nTraining score:", model.score(X_train, y_train))
    print("Test accuracy: ", metrics.accuracy_score(y_test, y_pred))

    class_names = encoders["class"].classes_
    print("\nConfusion matrix:")
    print(metrics.confusion_matrix(y_test, y_pred))
    print()
    print(
        metrics.classification_report(
            y_test,
            y_pred,
            target_names=class_names,
        )
    )

    # Step 8: Compare different tree depths
    results = []
    for depth in range(1, 13):
        clf_try = DecisionTreeClassifier(
            criterion="entropy",
            max_depth=depth,
            random_state=1,
        )
        clf_try.fit(X_train, y_train)
        results.append(
            (
                depth,
                clf_try.score(X_train, y_train),
                metrics.accuracy_score(
                    y_test,
                    clf_try.predict(X_test),
                ),
            )
        )

    results_df = pd.DataFrame(
        results,
        columns=["max_depth", "train_score", "test_accuracy"],
    )
    print("\nAccuracy by maximum tree depth:")
    print(results_df)

    plt.figure(figsize=(7, 4))
    plt.plot(
        results_df["max_depth"],
        results_df["train_score"],
        marker="o",
        label="Training score",
    )
    plt.plot(
        results_df["max_depth"],
        results_df["test_accuracy"],
        marker="o",
        label="Test accuracy",
    )
    plt.xlabel("max_depth")
    plt.ylabel("Score")
    plt.title("Effect of max_depth on accuracy")
    plt.legend()
    plt.grid(True)
    plt.show()

    # Step 9: Train the final pruned model
    clf = DecisionTreeClassifier(
        criterion="entropy",
        max_depth=5,
        random_state=1,
    )
    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)
    print("\nFinal model training score:", clf.score(X_train, y_train))
    print(
        "Final model test accuracy: ",
        metrics.accuracy_score(y_test, y_pred),
    )
    print()
    print(
        metrics.classification_report(
            y_test,
            y_pred,
            target_names=class_names,
            zero_division=0,
        )
    )

    # Step 10: Visualize the decision tree
    plt.figure(figsize=(24, 10))
    plot_tree(
        clf,
        feature_names=X.columns,
        class_names=class_names,
        filled=True,
        rounded=True,
        fontsize=8,
    )
    plt.show()

    # Step 11: Display feature importance
    importance = pd.Series(
        clf.feature_importances_,
        index=X.columns,
    ).sort_values(ascending=False)
    print("\nFeature importance:")
    print(importance)

    importance.plot(
        kind="bar",
        figsize=(7, 4),
        title="Feature importance",
    )
    plt.show()

    # Step 12: Predict ratings for new cars
    def predict_car(buying, maint, doors, persons, lug_boot, safety):
        row = pd.DataFrame(
            [
                [
                    encoders["buying"].transform([buying])[0],
                    encoders["maint"].transform([maint])[0],
                    encoders["doors"].transform([doors])[0],
                    encoders["persons"].transform([persons])[0],
                    encoders["lug_boot"].transform([lug_boot])[0],
                    encoders["safety"].transform([safety])[0],
                ]
            ],
            columns=X.columns,
        )
        prediction = clf.predict(row)
        return encoders["class"].inverse_transform(prediction)[0]

    print(
        "\nCar 1:",
        predict_car("low", "low", "4", "4", "big", "high"),
    )
    print(
        "Car 2:",
        predict_car("low", "low", "4", "4", "big", "low"),
    )
    print(
        "Car 3:",
        predict_car("vhigh", "vhigh", "2", "2", "small", "med"),
    )


if __name__ == "__main__":
    main()
