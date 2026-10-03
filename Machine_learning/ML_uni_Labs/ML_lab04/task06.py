import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split

"""Load the built-in digits dataset"""
digits = load_digits()

"""Display first 5 digit images"""
plt.figure(figsize=(12, 4))
for i in range(5):
    plt.subplot(1, 5, i + 1)
    plt.imshow(digits.images[i], cmap='gray')
    plt.axis('off')
plt.suptitle('Sample Digits')
plt.show()

"""Prepare data"""
X_train, X_test, y_train, y_test = train_test_split(
    digits.data,
    digits.target,
    test_size=0.2,
    random_state=42,
    stratify=digits.target,
)

"""Train logistic regression model"""
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

"""Evaluate model"""
accuracy = model.score(X_test, y_test)
print('Accuracy:', accuracy)
print('Sample predictions:', model.predict(digits.data[:5]))

"""Confusion Matrix"""
y_predicted = model.predict(X_test)
cm = confusion_matrix(y_test, y_predicted)
print(cm)

plt.figure(figsize=(10, 7))
plt.imshow(cm, cmap='Blues')
plt.colorbar()
for i in range(cm.shape[0]):
    for j in range(cm.shape[1]):
        plt.text(j, i, cm[i, j], ha='center', va='center', color='white' if cm[i, j] > cm.max() / 2 else 'black')
plt.xlabel('Predicted')
plt.ylabel('Truth')
plt.title('Digit Classification Confusion Matrix')
plt.xticks(range(cm.shape[1]))
plt.yticks(range(cm.shape[0]))
plt.show()
