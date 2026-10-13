

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier, plot_tree


DATA_FILE = Path(__file__).with_name("train.csv")


def main():
    # Step 2: Load the dataset
    if not DATA_FILE.exists():
        raise FileNotFoundError(
            f"Could not find {DATA_FILE.name}. Place it in {DATA_FILE.parent}."
        )

    df = pd.read_csv(DATA_FILE)
    print(df.head())

    # Step 3: Explore the data
    print("Shape:", df.shape)
    df.info()
    print("\nMissing values per column:")
    print(df.isnull().sum())

    # Step 4: Clean the data
    df = df.drop(
        ["PassengerId", "Name", "Ticket", "Cabin"],
        axis="columns",
    )
    df["Age"] = df["Age"].fillna(df["Age"].median())
    df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

    print("\nMissing values after cleaning:")
    print(df.isnull().sum())

    # Step 5: Encode text columns
    le_sex = LabelEncoder()
    le_embarked = LabelEncoder()

    df["Sex"] = le_sex.fit_transform(df["Sex"])
    df["Embarked"] = le_embarked.fit_transform(df["Embarked"])

    print(
        "Sex mapping:     ",
        dict(zip(le_sex.classes_, le_sex.transform(le_sex.classes_))),
    )
    print(
        "Embarked mapping:",
        dict(
            zip(
                le_embarked.classes_,
                le_embarked.transform(le_embarked.classes_),
            )
        ),
    )
    print(df.head())

    # Step 6: Separate features and target, then split the data
    X = df.drop("Survived", axis="columns")
    y = df["Survived"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.3,
        random_state=1,
    )

    print("Training samples:", X_train.shape[0])
    print("Testing samples: ", X_test.shape[0])

    # Step 7: Build and train the unpruned decision tree
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)

    # Step 8: Calculate the score of the unpruned model
    train_score = model.score(X_train, y_train)
    y_pred = model.predict(X_test)
    test_accuracy = metrics.accuracy_score(y_test, y_pred)

    print("Training score:", train_score)
    print("Test accuracy: ", test_accuracy)
    print("\nConfusion matrix:")
    print(metrics.confusion_matrix(y_test, y_pred))
    print()
    print(
        metrics.classification_report(
            y_test,
            y_pred,
            target_names=["Died", "Survived"],
        )
    )

    # Step 9: Compare different tree depths
    results = []
    for depth in range(1, 11):
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
                metrics.accuracy_score(y_test, clf_try.predict(X_test)),
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

    # Step 10: Train the final pruned model
    clf = DecisionTreeClassifier(
        criterion="entropy",
        max_depth=3,
        random_state=1,
    )
    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)
    print("Pruned model training score:", clf.score(X_train, y_train))
    print(
        "Pruned model test accuracy: ",
        metrics.accuracy_score(y_test, y_pred),
    )

    # Step 11: Visualize the decision tree
    plt.figure(figsize=(20, 9))
    plot_tree(
        clf,
        feature_names=X.columns,
        class_names=["Died", "Survived"],
        filled=True,
        rounded=True,
        fontsize=10,
    )
    plt.show()

    # Step 12: Display feature importance
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

    # Step 13: Predict survival for new passengers
    # Feature order: Pclass, Sex, Age, SibSp, Parch, Fare, Embarked.
    p1 = pd.DataFrame(
        [[3, 1, 22, 1, 0, 7.25, 2]],
        columns=X.columns,
    )
    p2 = pd.DataFrame(
        [[1, 0, 38, 1, 0, 71.28, 0]],
        columns=X.columns,
    )

    for name, passenger in [
        ("Passenger 1 (3rd class man, 22)", p1),
        ("Passenger 2 (1st class woman, 38)", p2),
    ]:
        result = clf.predict(passenger)[0]
        prediction = "Survived" if result == 1 else "Did not survive"
        print(name, "->", prediction)


if __name__ == "__main__":
    main()
