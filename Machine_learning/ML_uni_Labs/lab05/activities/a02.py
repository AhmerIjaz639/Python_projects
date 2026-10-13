# Activity 1: Classification of Iris flower dataset - Gaussian Naive Bayes
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics

iris = load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=0)

gnb = GaussianNB()
gnb.fit(X_train, y_train)

y_pred = gnb.predict(X_test)
accuracy = metrics.accuracy_score(y_test, y_pred)
print("Gaussian Naive Bayes model accuracy (in %):", accuracy * 100)

# Activity 2: Classifying Text - Multinomial Naive Bayes
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score

categories = ['talk.religion.misc', 'soc.religion.christian', 'comp.graphics', 'sci.space']

train = fetch_20newsgroups(subset='train', categories=categories, shuffle=True, random_state=42)
test = fetch_20newsgroups(subset='test', categories=categories, shuffle=True, random_state=42)

print("Training categories:", train.target_names)
print("Sample training document:\n", train.data[0])

model = make_pipeline(TfidfVectorizer(), MultinomialNB())
model.fit(train.data, train.target)

predicted = model.predict(test.data)
print("Multinomial Naive Bayes accuracy:", accuracy_score(test.target, predicted))
