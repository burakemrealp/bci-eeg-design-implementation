import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

# Load features and labels
X = np.load("data/processed/features.npy")
y = np.load("data/processed/labels.npy")

# Reshape for sklearn
X = X.reshape(-1, 1)

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train SVM
clf = SVC(kernel="rbf")
clf.fit(X_train, y_train)

# Predict
y_pred = clf.predict(X_test)

print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix:\n")
print(confusion_matrix(y_test, y_pred))
