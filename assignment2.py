# -*- coding: utf-8 -*-
"""Assignment2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10c3D5o1fw5AvLbxIqcUXDcdF6ash3yp8
"""

from sklearn import datasets

# Load the Iris dataset
iris = datasets.load_iris()
data = iris.data
target = iris.target
feature_names = iris.feature_names

# Now you can access the feature names
print("Feature Names:", feature_names)

#import my dataset into Google Colab
from google.colab import files
uploaded = files.upload()

#display my dataset with the first 5 rows
import pandas as pd

# Read the CSV file from the current working directory
data = pd.read_csv('IRIS - IRIS.csv')

# Display the first 5 rows of the DataFrame
data.head(5)

# Load the Iris dataset
from sklearn.datasets import load_iris
iris = load_iris()
X = iris.data
y = iris.target

# Split the data into a training set and a test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Decision Tree classifier
from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier()

# Train the classifier on the training data
clf.fit(X_train, y_train)

# Make predictions on the test data
y_pred = clf.predict(X_test)

# Calculate Mean Squared Error (MSE) without scikit-learn
def mean_squared_error(y_true, y_pred):
    if len(y_true) != len(y_pred):
        raise ValueError("Input arrays must have the same length.")

    squared_diff_sum = sum((y_true[i] - y_pred[i]) ** 2 for i in range(len(y_true)))
    mse = squared_diff_sum / len(y_true)
    return mse

# Calculate the MSE between y_test and y_pred
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error (Loss):", mse)

#Generate a visual representation of Decision Tree
import pandas as pd

# Load the dataset
data = pd.DataFrame({
    'sepal-length': [5.1, 4.9, 4.7, 4.6, 5.0],
    'sepal-width': [3.5, 3.0, 3.2, 3.1, 3.6],
    'petal-length': [1.4, 1.4, 1.3, 1.5, 1.4],
    'petal-width': [0.2, 0.2, 0.2, 0.2, 0.2],
    'species': ['Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa']
})

# Separate features (X) and target (y)
X = data.drop(columns=['species'])
y = data['species']

from sklearn.tree import DecisionTreeClassifier

# Create a Decision Tree classifier
clf = DecisionTreeClassifier()

# Train the classifier on the data
clf.fit(X, y)

from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 6))
plot_tree(clf, filled=True, feature_names=X.columns, class_names=y.unique())
plt.show()

import pandas as pd
import numpy as np

# Load the dataset #new one
data = pd.DataFrame({
    'sepal-length': [5.1, 4.9, 4.7, 4.6, 5.0],
    'sepal-width': [3.5, 3.0, 3.2, 3.1, 3.6],
    'petal-length': [1.4, 1.4, 1.3, 1.5, 1.4],
    'petal-width': [0.2, 0.2, 0.2, 0.2, 0.2],
    'species': ['Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa']
})

# Separate features (X) and target (y)
X = data.drop(columns=['species'])
y = data['species']

# Split the data into a training set and a test set
np.random.seed(0)  # For reproducibility
indices = np.arange(len(data))
np.random.shuffle(indices)
split_index = int(0.8 * len(data))
X_train, X_test = X.iloc[indices[:split_index]], X.iloc[indices[split_index:]]
y_train, y_test = y.iloc[indices[:split_index]], y.iloc[indices[split_index:]]

# Define a function to calculate accuracy
def calculate_accuracy(y_true, y_pred):
    correct = np.sum(y_true == y_pred)
    total = len(y_true)
    return correct / total

# Define a function to calculate precision
def calculate_precision(y_true, y_pred, target_class):
    true_positives = np.sum((y_true == target_class) & (y_pred == target_class))
    predicted_positives = np.sum(y_pred == target_class)
    return true_positives / predicted_positives if predicted_positives > 0 else 0

# Define a function to calculate recall
def calculate_recall(y_true, y_pred, target_class):
    true_positives = np.sum((y_true == target_class) & (y_pred == target_class))
    actual_positives = np.sum(y_true == target_class)
    return true_positives / actual_positives if actual_positives > 0 else 0

# Define a function to calculate F1-score
def calculate_f1_score(y_true, y_pred, target_class):
    precision = calculate_precision(y_true, y_pred, target_class)
    recall = calculate_recall(y_true, y_pred, target_class)
    return 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0

# Calculate accuracy
y_pred = ['Iris-setosa'] * len(y_test)  # Replace this with your actual predictions
accuracy = calculate_accuracy(y_test, y_pred)
print("Accuracy:", accuracy)

# Calculate precision, recall, and F1-score for 'Iris-setosa' class
target_class = 'Iris-setosa'
precision = calculate_precision(y_test, y_pred, target_class)
recall = calculate_recall(y_test, y_pred, target_class)
f1_score = calculate_f1_score(y_test, y_pred, target_class)
print("Precision:", precision)
print("Recall:", recall)
print("F1-Score:", f1_score)

# Calculate the confusion matrix
unique_classes = y_test.unique()
confusion = np.zeros((len(unique_classes), len(unique_classes)), dtype=int)
for i, true_class in enumerate(unique_classes):
    for j, predicted_class in enumerate(unique_classes):
        confusion[i][j] = np.sum((y_test == true_class) & (y_pred == predicted_class))

print("Confusion Matrix:")
print(confusion)

import numpy as np

# Define a function to calculate accuracy #new one
def calculate_accuracy(y_true, y_pred):
    correct = np.sum(y_true == y_pred)
    total = len(y_true)
    return correct / total

# Define a function to calculate precision
def calculate_precision(y_true, y_pred, target_class):
    true_positives = np.sum((y_true == target_class) & (y_pred == target_class))
    predicted_positives = np.sum(y_pred == target_class)
    return true_positives / predicted_positives if predicted_positives > 0 else 0

# Define a function to calculate recall
def calculate_recall(y_true, y_pred, target_class):
    true_positives = np.sum((y_true == target_class) & (y_pred == target_class))
    actual_positives = np.sum(y_true == target_class)
    return true_positives / actual_positives if actual_positives > 0 else 0

# Define a function to calculate F1-score
def calculate_f1_score(y_true, y_pred, target_class):
    precision = calculate_precision(y_true, y_pred, target_class)
    recall = calculate_recall(y_true, y_pred, target_class)
    return 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0

# Define a function to calculate confusion matrix
def calculate_confusion_matrix(y_true, y_pred, num_classes):
    confusion = np.zeros((num_classes, num_classes), dtype=int)
    for i in range(num_classes):
        for j in range(num_classes):
            confusion[i][j] = np.sum((y_true == i) & (y_pred == j))
    return confusion

# Load the Iris dataset
from sklearn.datasets import load_iris
iris = load_iris()
X = iris.data
y = iris.target

# Split the data into a training set and a test set
np.random.seed(0)  # For reproducibility
indices = np.arange(len(X))
np.random.shuffle(indices)
split_index = int(0.8 * len(X))
X_train, X_test = X[indices[:split_index]], X[indices[split_index:]]
y_train, y_test = y[indices[:split_index]], y[indices[split_index:]]

# Create a Decision Tree classifier
class DecisionTreeClassifier:
    def fit(self, X, y):
        self.X = X
        self.y = y

    def predict(self, X):
        return np.random.choice(self.y, len(X))

clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

# Make predictions on the test data
y_pred = clf.predict(X_test)

# Calculate accuracy
accuracy = calculate_accuracy(y_test, y_pred)
print("Accuracy:", accuracy)

# Calculate precision, recall, F1-score, and support for each class
unique_classes = np.unique(y_test)
for target_class in unique_classes:
    precision = calculate_precision(y_test, y_pred, target_class)
    recall = calculate_recall(y_test, y_pred, target_class)
    f1_score = calculate_f1_score(y_test, y_pred, target_class)
    support = np.sum(y_test == target_class)
    print(f"Class {target_class}:")
    print("  Precision:", precision)
    print("  Recall:", recall)
    print("  F1-Score:", f1_score)
    print("  Support:", support)

# Calculate the confusion matrix
confusion = calculate_confusion_matrix(y_test, y_pred, num_classes=len(unique_classes))
print("Confusion Matrix:\n", confusion)

import pandas as pd

# Read the CSV file from the current working directory
data = pd.read_csv('IRIS - IRIS.csv')

# Display the first 5 rows of the DataFrame
data.head(20)

#Calculate accuracy, classification reports, and confusion matrix
import pandas as pd
import numpy as np

# Load the dataset #new one
data = pd.DataFrame({
    'sepal-length': [5.1, 4.9, 4.7, 4.6, 5.0],
    'sepal-width': [3.5, 3.0, 3.2, 3.1, 3.6],
    'petal-length': [1.4, 1.4, 1.3, 1.5, 1.4],
    'petal-width': [0.2, 0.2, 0.2, 0.2, 0.2],
    'species': ['Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa']
})

# Separate features (X) and target (y)
X = data.drop(columns=['species'])
y = data['species']

# Split the data into a training set and a test set
np.random.seed(0)  # For reproducibility
indices = np.arange(len(data))
np.random.shuffle(indices)
split_index = int(0.8 * len(data))
X_train, X_test = X.iloc[indices[:split_index]], X.iloc[indices[split_index:]]
y_train, y_test = y.iloc[indices[:split_index]], y.iloc[indices[split_index:]]

# Create a mapping from string labels to integer labels
label_mapping = {label: i for i, label in enumerate(y_train.unique())}

# Convert string labels to integer labels
y_train = y_train.map(label_mapping)
y_test = y_test.map(label_mapping)

# Implement a function to calculate information gain
def calculate_information_gain(y, mask):
    if len(y) == 0:
        return 0
    p_i = np.bincount(y[mask]) / len(y)
    entropy_parent = -np.sum(p_i * np.log2(p_i + (p_i == 0)))
    entropy_children = 0
    for m in [True, False]:
        if len(y[mask & (y == m)]) == 0:
            continue
        p_i = np.bincount(y[mask & (y == m)]) / len(y[mask])
        entropy_children += (len(y[mask & (y == m)]) / len(y[mask])) * -np.sum(p_i * np.log2(p_i + (p_i == 0)))
    return entropy_parent - entropy_children

# Implement a function to predict using the decision tree
def predict_tree(tree, X):
    if tree['is_leaf']:
        return tree['class']

    if X[tree['split_feature']] < tree['split_value']:
        return predict_tree(tree['left'], X)
    else:
        return predict_tree(tree['right'], X)

# Build the decision tree
def decision_tree(X, y, max_depth=None):
    if max_depth == 0 or len(np.unique(y)) == 1:
        # If we reached the maximum depth or all samples have the same class, create a leaf node.
        return {'class': np.argmax(np.bincount(y)), 'is_leaf': True}

    # Find the best split based on information gain
    best_split = None
    best_information_gain = -1

    for col in X.columns:
        values = X[col].unique()
        for value in values:
            left_mask = X[col] < value
            right_mask = X[col] >= value
            left_information_gain = calculate_information_gain(y, left_mask)
            right_information_gain = calculate_information_gain(y, right_mask)
            weighted_information_gain = (len(left_mask) * left_information_gain + len(right_mask) * right_information_gain) / len(X)
            if weighted_information_gain > best_information_gain:
                best_information_gain = weighted_information_gain
                best_split = (col, value, left_mask, right_mask)

    if best_split is None:
        # If no split improves the information gain, create a leaf node.
        return {'class': np.argmax(np.bincount(y)), 'is_leaf': True}

    # Recursively build the tree
    left_subtree = decision_tree(X[best_split[2]], y[left_split], max_depth - 1 if max_depth is not None else None)
    right_subtree = decision_tree(X[best_split[3]], y[right_split], max_depth - 1 if max_depth is not None else None)

    return {'is_leaf': False, 'split_feature': best_split[0], 'split_value': best_split[1], 'left': left_subtree, 'right': right_subtree}

tree = decision_tree(X_train, y_train, max_depth=None)

# Make predictions
y_pred = X_test.apply(lambda x: predict_tree(tree, x), axis=1)

#def accuracy_score(y_true, y_pred, *, normalize=True, sample_weight=None)

# Calculate accuracy
accuracy = accuracy_score(y_true=y_test, y_pred=y_pred)

print("Accuracy:", accuracy)


#def classification_report(y_true, y_pred, *, labels=None, target_names=None, sample_weight=None, digits=2, output_dict=False, zero_division='warn')
# Print classification report (includes precision, recall, F1-score)
print(classification_report(y_test, y_pred))

#def confusion_matrix(y_true, y_pred, *, labels=None, sample_weight=None, normalize=None)
# Display the confusion matrix
confusion = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:\n", confusion)

# Visualize the Decision Tree
plt.figure(figsize=(12, 6))
plot_tree(clf, filled=True, feature_names=X.columns, class_names=y.unique())
plt.show()

#data visualisation
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your dataset
data = pd.read_csv('IRIS - IRIS.csv')

# Count the number of samples in each class
class_counts = data['species'].value_counts()

# Plot the class distribution
plt.figure(figsize=(8, 6))
sns.countplot(data=data, x='species')
plt.title('Class Distribution')
plt.xlabel('Species')
plt.ylabel('Count')
plt.show()

# Print class counts
print(class_counts)

#import my dataset into Google Colab again
from google.colab import files
uploaded = files.upload()

#Hyperparameter
import pandas as pd
import numpy as np

# Load the dataset
data = pd.DataFrame({
    'sepal-length': [5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4, 4.9, 5.4, 4.8, 4.8, 4.3, 5.8, 5.7, 5.4, 5.1, 5.7, 5.1],
    'sepal-width': [3.5, 3.0, 3.2, 3.1, 3.6, 3.9, 3.4, 3.4, 2.9, 3.1, 3.7, 3.4, 3.0, 3.0, 4.0, 4.4, 3.9, 3.5, 3.8, 3.8],
    'petal-length': [1.4, 1.4, 1.3, 1.5, 1.4, 1.7, 1.4, 1.5, 1.4, 1.5, 1.5, 1.6, 1.4, 1.1, 1.2, 1.5, 1.3, 1.4, 1.7, 1.5],
    'petal-width': [0.2, 0.2, 0.2, 0.2, 0.2, 0.4, 0.3, 0.2, 0.2, 0.1, 0.2, 0.2, 0.1, 0.1, 0.2, 0.4, 0.4, 0.3, 0.3, 0.3],
    'species': ['Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa']
})

# Separate features (X) and target (y)
X = data.drop(columns=['species'])
y = data['species']

# Split the data into a training set and a test set
np.random.seed(0)  # For reproducibility
indices = np.arange(len(data))
np.random.shuffle(indices)
split_index = int(0.8 * len(data))
X_train, X_test = X.iloc[indices[:split_index]], X.iloc[indices[split_index:]]
y_train, y_test = y.iloc[indices[:split_index]], y.iloc[indices[split_index:]]

# Define hyperparameter combinations to search
max_depth_values = [None, 5, 10, 15]
min_samples_split_values = [2, 5, 10]
min_samples_leaf_values = [1, 2, 4]
criterion_values = ['gini', 'entropy']

best_accuracy = 0
best_params = {}

# Implement a basic decision tree manually
def decision_tree(X, y, max_depth=None, min_samples_split=2, min_samples_leaf=1, criterion='gini'):
    if max_depth == 0 or len(np.unique(y)) == 1:
        # If we reached the maximum depth or all samples have the same class, create a leaf node.
        return {'class': np.argmax(np.bincount(y)), 'is_leaf': True}

    if len(X) < min_samples_split:
        # If the number of samples is less than min_samples_split, create a leaf node.
        return {'class': np.argmax(np.bincount(y)), 'is_leaf': True}

    # Find the best split based on criterion
    best_split = None
    best_split_criterion = -1

    for col in X.columns:
        values = X[col].unique()
        for value in values:
            left_mask = X[col] < value
            right_mask = X[col] >= value
            left_criterion = calculate_criterion(y[left_mask], criterion)
            right_criterion = calculate_criterion(y[right_mask], criterion)
            weighted_criterion = (len(left_mask) * left_criterion + len(right_mask) * right_criterion) / len(X)
            if weighted_criterion > best_split_criterion:
                best_split_criterion = weighted_criterion
                best_split = (col, value, left_mask, right_mask)

    if best_split is None:
        # If no split improves the criterion, create a leaf node.
        return {'class': np.argmax(np.bincount(y)), 'is_leaf': True}

    # Recursively build the tree
    left_subtree = decision_tree(X[best_split[2]], y[best_split[2]], max_depth - 1 if max_depth is not None else None, min_samples_split, min_samples_leaf, criterion)
    right_subtree = decision_tree(X[best_split[3]], y[best_split[3]], max_depth - 1 if max_depth is not None else None, min_samples_split, min_samples_leaf, criterion)

    return {'is_leaf': False, 'split_feature': best_split[0], 'split_value': best_split[1], 'left': left_subtree, 'right': right_subtree}

# Implement a function to calculate criterion (Gini or Entropy)
def calculate_criterion(y, criterion='gini'):
    n = len(y)
    if n == 0:
        return 0
    p_i = np.bincount(y) / n
    if criterion == 'gini':
        return 1 - np.sum(p_i ** 2)
    elif criterion == 'entropy':
        return -np.sum(p_i * np.log2(p_i))
    else:
        raise ValueError("Invalid criterion")

# Implement a function to predict using the decision tree
# ... (previous code)

# Implement a function to predict using the decision tree
def predict_tree(tree, X):
    if tree['is_leaf']:
        return tree['class']

    if X[tree['split_feature']] < tree['split_value']:
        return predict_tree(tree['left'], X)
    else:
        return predict_tree(tree['right'], X)

# Encode the target variable 'species'
from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()
y_train_encoded = label_encoder.fit_transform(y_train)
y_test_encoded = label_encoder.transform(y_test)

# Perform grid search manually
for max_depth, min_samples_split, min_samples_leaf, criterion in product(max_depth_values, min_samples_split_values, min_samples_leaf_values, criterion_values):
    tree = decision_tree(X_train, y_train_encoded, max_depth, min_samples_split, min_samples_leaf, criterion)
    y_pred = X_test.apply(lambda x: predict_tree(tree, x), axis=1)
    accuracy = accuracy_score(y_test_encoded, y_pred)

    if accuracy > best_accuracy:
        best_accuracy = accuracy
        best_params = {
            'max_depth': max_depth,
            'min_samples_split': min_samples_split,
            'min_samples_leaf': min_samples_leaf,
            'criterion': criterion
        }

# Train a decision tree with the best hyperparameters
best_tree = decision_tree(X_train, y_train_encoded, best_params['max_depth'], best_params['min_samples_split'], best_params['min_samples_leaf'], best_params['criterion'])

# Make predictions
y_pred = X_test.apply(lambda x: predict_tree(best_tree, x), axis=1)

# Calculate the accuracy
accuracy = accuracy_score(y_test_encoded, y_pred)

print("Best Hyperparameters:", best_params)
print("Accuracy with Best Hyperparameters:", accuracy)

#Perform oversampling using SMOTE manually #new one
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

# Load your dataset
data = pd.read_csv('IRIS - IRIS.csv')

# Separate features (X) and target (y)
X = data.drop(columns=['species'])
y = data['species']

# Split the data into a training set and a test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Find the minority class
minority_class = y_train.value_counts().idxmin()

# Split the training data into minority and majority classes
X_minority = X_train[y_train == minority_class]
X_majority = X_train[y_train != minority_class]
y_minority = y_train[y_train == minority_class]
y_majority = y_train[y_train != minority_class]

# Determine the number of samples to generate to balance the classes
n_minority = len(X_minority)
n_majority = len(X_majority)
n_samples_to_generate = n_majority - n_minority

# Create synthetic samples for the minority class
synthetic_samples = []
for _ in range(n_samples_to_generate):
    # Randomly select a minority sample
    idx = np.random.randint(0, n_minority)
    minority_sample = X_minority.iloc[idx]

    # Randomly select one of its k-nearest neighbors
    k = 5  # You can adjust k as needed
    distances = np.linalg.norm(X_minority - minority_sample, axis=1)
    nearest_neighbor_idx = np.argpartition(distances, k)[1]
    nearest_neighbor = X_minority.iloc[nearest_neighbor_idx]

    # Generate a synthetic sample
    alpha = np.random.uniform(0, 1)
    synthetic_sample = minority_sample + alpha * (nearest_neighbor - minority_sample)

    synthetic_samples.append(synthetic_sample)

# Add the synthetic samples to the minority class
X_minority_resampled = pd.concat([X_minority, pd.DataFrame(synthetic_samples, columns=X.columns)], ignore_index=True)
y_minority_resampled = pd.concat([y_minority, pd.Series([minority_class] * n_samples_to_generate)], ignore_index=True)

# Combine the resampled minority class and majority class
X_train_resampled = pd.concat([X_minority_resampled, X_majority], axis=0, ignore_index=True)
y_train_resampled = pd.concat([y_minority_resampled, y_majority], axis=0, ignore_index=True)

#Calculate Feature Importance #new one
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load your dataset
data = pd.read_csv('IRIS - IRIS.csv')

# Separate features (X) and target (y)
X = data.drop('species', axis=1)
y = data['species']

# Define a function to calculate Gini importance
def calculate_feature_importance(X, y, feature_name):
    gini_importance = 0
    unique_classes = y.unique()

    for feature_value in X[feature_name].unique():
        feature_indices = X[feature_name] == feature_value
        probabilities = [(y[feature_indices] == cls).mean() for cls in unique_classes]
        squared_probabilities = [p ** 2 for p in probabilities]
        gini_importance += sum(squared_probabilities) * (1 - sum(squared_probabilities))

    return gini_importance

# Calculate feature importance for each feature
feature_importances = {feature: calculate_feature_importance(X, y, feature) for feature in X.columns}

# Sort feature importances
sorted_feature_importances = dict(sorted(feature_importances.items(), key=lambda item: item[1], reverse=True))

# Visualize feature importances
plt.figure(figsize=(8, 6))
plt.bar(sorted_feature_importances.keys(), sorted_feature_importances.values())
plt.title('Feature Importance (Gini Importance)')
plt.xlabel('Features')
plt.ylabel('Importance')
plt.xticks(rotation=45)
plt.show()

#Pruning technique #new one
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load your dataset
data = pd.read_csv('IRIS - IRIS.csv')

# Separate features (X) and target (y)
X = data.drop(columns=['species'])
y = data['species']

# Encode the target variable into numerical values
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)

# Define a function to calculate the Gini impurity
def gini_impurity(y):
    if len(y) == 0:
        return 0
    p_i = np.bincount(y) / len(y)
    return 1 - np.sum(p_i ** 2)

# Define a function to recursively build a decision tree
def build_tree(X, y, depth, max_depth):
    if depth >= max_depth or gini_impurity(y) == 0:
        # Create a leaf node
        return {'class': np.argmax(np.bincount(y)), 'is_leaf': True}
    else:
        # Find the best split
        best_gini = 1.0
        best_split = None
        for column in X.columns:
            values = X[column].unique()
            for value in values:
                left_mask = X[column] < value
                right_mask = X[column] >= value
                left_gini = gini_impurity(y[left_mask])
                right_gini = gini_impurity(y[right_mask])
                weighted_gini = (len(y[left_mask]) / len(y)) * left_gini + (len(y[right_mask]) / len(y)) * right_gini
                if weighted_gini < best_gini:
                    best_gini = weighted_gini
                    best_split = (column, value, left_mask, right_mask)

        if best_split is not None:
            left_tree = build_tree(X[best_split[2]], y[best_split[2]], depth + 1, max_depth)
            right_tree = build_tree(X[best_split[3]], y[best_split[3]], depth + 1, max_depth)
            return {'is_leaf': False, 'split_feature': best_split[0], 'split_value': best_split[1], 'left': left_tree, 'right': right_tree}

# Build the decision tree
max_depth = 5  # You can adjust the maximum depth
tree = build_tree(X, y, depth=0, max_depth=max_depth)

# Visualize the tree structure (simplified)
def visualize_tree(tree, depth=0):
    if tree['is_leaf']:
        print(f"{depth * '  '}Leaf Node: Class {label_encoder.classes_[tree['class']]}")
    else:
        print(f"{depth * '  '}{tree['split_feature']} < {tree['split_value']}?")
        visualize_tree(tree['left'], depth + 1)
        visualize_tree(tree['right'], depth + 1)

# Visualize the tree structure
visualize_tree(tree)

#Ensemble Method using Random Forest #new one
import numpy as np
import pandas as pd

# Load your dataset
data = pd.read_csv('IRIS - IRIS.csv')

# Separate features (X) and target (y)
X = data.drop(columns=['species'])
y = data['species']

# Encode the target variable into numerical values
from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)

# Define a function to calculate the Gini impurity
def gini_impurity(y):
    if len(y) == 0:
        return 0
    p_i = np.bincount(y) / len(y)
    return 1 - np.sum(p_i ** 2)

# Define a function to recursively build a decision tree
def build_tree(X, y, depth, max_depth, max_features):
    if depth >= max_depth or gini_impurity(y) == 0:
      if len(y) == 0:
        return {'class': None, 'is_leaf': True}
      else:
        # Create a leaf node
          return {'class': np.argmax(np.bincount(y)), 'is_leaf': True}
    else:
        # Find the best split
        best_gini = 1.0
        best_split = None

        # Randomly select a subset of features for consideration
        features = np.random.choice(X.columns, max_features, replace=False)

        for column in features:
            values = X[column].unique()
            for value in values:
                left_mask = X[column] < value
                right_mask = X[column] >= value
                left_gini = gini_impurity(y[left_mask])
                right_gini = gini_impurity(y[right_mask])
                weighted_gini = (len(y[left_mask]) / len(y)) * left_gini + (len(y[right_mask]) / len(y)) * right_gini
                if weighted_gini < best_gini:
                    best_gini = weighted_gini
                    best_split = (column, value, left_mask, right_mask)

        if best_split is not None:
            left_tree = build_tree(X[best_split[2]], y[best_split[2]], depth + 1, max_depth, max_features)
            right_tree = build_tree(X[best_split[3]], y[best_split[3]], depth + 1, max_depth, max_features)
            return {'is_leaf': False, 'split_feature': best_split[0], 'split_value': best_split[1], 'left': left_tree, 'right': right_tree}

# Define a function to make predictions using the decision tree
def predict_tree(tree, X):
    if tree['is_leaf']:
        return tree['class']

    if (X[tree['split_feature']] < tree['split_value']).all():
        return predict_tree(tree['left'], X)
    else:
        return predict_tree(tree['right'], X)

# Define a function to build an ensemble of decision trees
def build_forest(X, y, n_trees, max_depth, max_features):
    forest = []
    for _ in range(n_trees):
        indices = np.random.choice(len(X), len(X), replace=True)
        X_subset, y_subset = X.iloc[indices], y[indices]
        tree = build_tree(X_subset, y_subset, depth=0, max_depth=max_depth, max_features=max_features)
        forest.append(tree)
    return forest

# Define a function to make predictions using the ensemble of trees
def predict_forest(forest, X):
    predictions = [predict_tree(tree, X) for tree in forest]
    return np.array(predictions)

# Build a Random Forest-like ensemble of decision trees
n_trees = 100  # Number of trees in the forest
max_depth = 5  # Maximum depth of each tree
max_features = 2  # Number of features to consider at each split
forest = build_forest(X, y, n_trees, max_depth, max_features)

# Make predictions using the ensemble
y_pred = predict_forest(forest, X)

# Calculate accuracy
accuracy = np.mean(y_pred == y)
print(f"Random Forest Accuracy: {accuracy:.2f}")

#Ensemble method using Gradient Boost Tree
import numpy as np
import pandas as pd

# Load your dataset #new one
data = pd.read_csv('IRIS - IRIS.csv')

# Separate features (X) and target (y)
X = data.drop(columns=['species'])
y = data['species']

# Define the number of estimators (number of weak learners)
n_estimators = 100

# Learning rate (shrinkage)
learning_rate = 0.1

# Initialize predictions with zeros for each class
n_classes = len(np.unique(y))
predictions = np.zeros((len(y), n_classes))

# Define a logistic function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Define a function to compute the logistic gradient
def logistic_gradient(y, predictions):
    return -2 * (y - sigmoid(predictions))

# Perform gradient boosting with basic decision stumps as weak learners
for _ in range(n_estimators):
    for class_label in range(n_classes):
        # Convert the problem into binary classification (class vs. not class)
        y_binary = (y == class_label).astype(int)

        # Compute the gradient
        gradient = logistic_gradient(y_binary, predictions[:, class_label])

        # Create a simple decision stump as a weak learner
        column = np.random.choice(X.columns)
        threshold = np.random.uniform(X[column].min(), X[column].max())

        # Make predictions with the decision stump
        weak_learner_predictions = (X[column] < threshold).astype(int)

        # Update the predictions for the current class with a fraction of the weak learner's predictions (learning_rate)
        predictions[:, class_label] += learning_rate * weak_learner_predictions * gradient

# Assign class labels based on the class with the highest prediction value
final_predictions = np.argmax(predictions, axis=1)

# Now you can evaluate the model's accuracy and other metrics using final_predictions

# Example: Calculate accuracy
accuracy = np.mean(final_predictions == y)
print(f'Gradient Boosting Accuracy: {accuracy:.2f}')

#Entropy function
import pandas as pd

# Assuming your dataset is stored in a CSV file named 'iris_dataset.csv'
# You can read the dataset into a Pandas DataFrame
df = pd.read_csv('IRIS - IRIS.csv')

# Extract the features (X) and target (y) as arrays
X = df[['sepal-length', 'sepal-width', 'petal-length', 'petal-width']].values
y = df['species'].values

import numpy as np

def entropy(y):
    unique, counts = np.unique(y, return_counts=True)
    probabilities = counts / len(y)
    entropy = -np.sum(probabilities * np.log2(probabilities))
    return entropy

# Example: Calculate entropy for a target variable (y)
entropy_score = entropy(y_train)
print("Entropy Score:", entropy_score)

#loss function
import numpy as np
from sklearn import tree

def cross_entropy(y_true, y_pred):
    """Calculates the cross-entropy loss function.

    Args:
        y_true: A numpy array of the true class labels.
        y_pred: A numpy array of the predicted class labels.

    Returns:
        A numpy float representing the cross-entropy loss.
    """

    # Calculate the predicted probability that each data point belongs to the class.
    p_pred = 1 / (1 + np.exp(-y_pred))

    # Calculate the cross-entropy loss function.
    loss = -np.sum(y_true * np.log(p_pred))

    return loss

# Create the Decision Tree model
clf = tree.DecisionTreeClassifier()

# Create the features and target arrays
features = np.array([
    [5.1, 3.5, 1.4, 0.2], [4.9, 3.0, 1.4, 0.2], [4.7, 3.2, 1.3, 0.2], [4.6, 3.1, 1.5, 0.2], [5.0, 3.6, 1.4, 0.2],
    [5.4, 3.9, 1.7, 0.4], [4.6, 3.4, 1.4, 0.3], [5.0, 3.4, 1.5, 0.2], [4.4, 2.9, 1.4, 0.2], [4.9, 3.1, 1.5, 0.1],
    [5.4, 3.7, 1.5, 0.2], [4.8, 3.4, 1.6, 0.2], [4.8, 3.0, 1.4, 0.1], [4.3, 3.0, 1.1, 0.1], [5.8, 4.0, 1.2, 0.2],
    [5.7, 4.4, 1.5, 0.4], [5.4, 3.9, 1.3, 0.4], [5.1, 3.5, 1.4, 0.3], [5.7, 3.8, 1.7, 0.3], [5.1, 3.8, 1.5, 0.3]
])

# Create the target array with 20 labels
target = np.array([
    0, 0, 0, 0, 0,
    0, 0, 0, 0, 0,
    1, 1, 1, 1, 1,
    1, 1, 1, 1, 1
])

# Train the model
clf.fit(features, target)

# Make a prediction for a sample
sample = [[5.1, 3.5, 1.4, 0.2]]
prediction = clf.predict(sample)

# Calculate the cross-entropy loss
loss = cross_entropy(target, prediction)

# Print the prediction and loss
print("Predicted class:", prediction[0])
print("The cross-entropy loss is:", loss)