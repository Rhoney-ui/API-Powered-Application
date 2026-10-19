# EXERCISE 3: FEATURE IMPORTANCE

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

print()
print("=== EXERCISE 3: FEATURE IMPORTANCE ===")
print()

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y)
model = DecisionTreeClassifier().fit(X_train, y_train)
features = load_iris().feature_names 
for name, imp in zip(features, model.feature_importances_):
    print(f"{name}: {imp:.3f}")