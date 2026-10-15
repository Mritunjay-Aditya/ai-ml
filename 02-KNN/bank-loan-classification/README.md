# Loan Approval Prediction using K-Nearest Neighbors (KNN)

## Project Overview

This project implements a **Loan Approval Prediction System** using the **K-Nearest Neighbors (KNN)** classification algorithm. The model predicts whether a customer is likely to receive a personal loan based on their demographic and financial information.

The dataset is automatically downloaded from Kaggle, preprocessed, used to train a KNN classifier, evaluated using various performance metrics, and finally deployed as a simple console-based prediction system.

---

# Dataset Information

Dataset Source:

https://www.kaggle.com/datasets/mitgandhi10/dataset-for-random-forest-regression

### Dataset Description

The dataset contains customer information from a banking institution. Each record represents an individual customer along with attributes that help determine whether they are likely to accept or qualify for a personal loan.

### Target Variable

| Column | Description |
|----------|-------------|
| Personal.Loan | Loan Status (0 = No, 1 = Yes) |

### Common Features

The dataset may contain:

- Age
- Experience
- Income
- Family
- CCAvg (Average Credit Card Spending)
- Education
- Mortgage
- Securities Account
- CD Account
- Online Banking
- Credit Card Usage
- ZIP Code
- ID

---

# Why KNN?

## What is KNN?

K-Nearest Neighbors (KNN) is a **supervised machine learning classification algorithm** that classifies new data points based on the majority class of their nearest neighbors.

The algorithm works on a simple idea:

1. Calculate the distance between the new data point and all training samples.
2. Find the K closest samples.
3. Count the class labels among those neighbors.
4. Assign the class that appears most frequently.

Example:

If K = 5 and among the 5 nearest neighbors:

- 4 customers received loans
- 1 customer did not receive a loan

Then the prediction will be:

```
Loan Approved
```

---

# Why KNN Was Used in This Project

KNN was selected because:

### 1. Classification Problem

The target variable (`Personal.Loan`) contains only two classes:

- 0 = No Loan
- 1 = Loan Approved

This makes KNN an appropriate classification algorithm.

### 2. Easy to Understand

KNN is one of the most intuitive machine learning algorithms and is excellent for educational and academic projects.

### 3. Works Well with Structured Data

The dataset contains numeric customer information, which is ideal for distance-based algorithms like KNN.

### 4. No Assumptions About Data Distribution

Unlike some machine learning algorithms, KNN does not assume:

- Normal distribution
- Linear relationships

This makes it flexible for real-world datasets.

### 5. Good Performance on Smaller Datasets

The banking dataset contains only a few thousand records, which allows KNN to perform efficiently while maintaining good accuracy.

---

# Why Scaling is Required

KNN calculates distances between features.

Example:

| Feature | Value |
|----------|--------|
| Income | 120 |
| Education | 2 |

Without scaling:

- Income dominates the distance calculation.
- Smaller-valued features become less important.

To solve this issue, the project uses:

```python
StandardScaler()
```

which standardizes features so they contribute equally to distance calculations.

---

# Data Preprocessing

Several preprocessing steps are performed before training.

## 1. Remove ID Column

```python
data = data.drop(columns=["ID"])
```

Reason:

- ID does not contain meaningful predictive information.

---

## 2. Remove ZIP.Code

```python
data = data.drop(columns=["ZIP.Code"])
```

Reason:

- ZIP codes are identifiers.
- Distance between ZIP codes is not meaningful.
- May negatively affect KNN performance.

---

## 3. Handle Missing Values

```python
data = data.dropna()
```

Reason:

- Missing values can cause errors during training.

---

## 4. Separate Features and Target

```python
X = data.drop(columns=["Personal.Loan"])
y = data["Personal.Loan"]
```

Where:

- X = Input features
- y = Output label

---

# Train-Test Split

The dataset is divided into:

- 80% Training Data
- 20% Testing Data

```python
train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)
```

### Why Stratify?

Stratification preserves the original class distribution in both training and testing datasets.

---

# Feature Scaling

```python
scaler = StandardScaler()
```

Training Data:

```python
X_train_scaled = scaler.fit_transform(X_train)
```

Testing Data:

```python
X_test_scaled = scaler.transform(X_test)
```

This ensures all features have comparable scales.

---

# Finding the Best K Value

Instead of choosing K randomly, the project tests multiple values.

```python
for k in range(1, max_k + 1):
```

For each value of K:

1. Train a KNN model.
2. Predict on the test set.
3. Calculate accuracy.
4. Store accuracy.

The value with the highest accuracy becomes the final K.

```python
best_k = accuracies.index(max(accuracies)) + 1
```

---

# Model Training

After selecting the optimal K:

```python
model = KNeighborsClassifier(
    n_neighbors=best_k
)
```

The model is trained:

```python
model.fit(
    X_train_scaled,
    y_train
)
```

---

# Model Evaluation

The project evaluates model performance using:

## Accuracy Score

```python
accuracy_score()
```

Measures:

```
Correct Predictions
-------------------
Total Predictions
```

---

## Confusion Matrix

```python
confusion_matrix()
```

Provides:

- True Positives
- True Negatives
- False Positives
- False Negatives

Example:

| Actual | Predicted |
|----------|-----------|
| Loan | Loan |
| Loan | No Loan |
| No Loan | Loan |
| No Loan | No Loan |

---

## Classification Report

```python
classification_report()
```

Includes:

- Precision
- Recall
- F1-Score
- Support

These metrics provide deeper insight than accuracy alone.

---

# Accuracy vs K Visualization

The project creates a graph showing how accuracy changes with different K values.

```python
plt.plot(
    range(1, max_k + 1),
    accuracies
)
```

Benefits:

- Helps identify optimal K.
- Visualizes model behavior.
- Prevents arbitrary parameter selection.

---

# Continuous Prediction System

After training, the project launches an interactive prediction mode.

Example:

```text
Enter Age: 35
Enter Income: 85
Enter Family: 3
...
```

The model:

1. Accepts user inputs.
2. Scales the inputs.
3. Predicts loan approval.
4. Displays prediction probability.

Output Example:

```text
Prediction Result:

Loan Approved

Predicted Class Probability:
92.50%
```

---

# Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-Learn
- KaggleHub

---

# Machine Learning Workflow

```text
Download Dataset
        │
        ▼
Load Dataset
        │
        ▼
Clean Data
        │
        ▼
Remove Unnecessary Columns
        │
        ▼
Handle Missing Values
        │
        ▼
Feature Scaling
        │
        ▼
Train-Test Split
        │
        ▼
Find Best K
        │
        ▼
Train KNN Model
        │
        ▼
Evaluate Model
        │
        ▼
Visualize Results
        │
        ▼
User Prediction System
```

---

# Conclusion

This project demonstrates how the K-Nearest Neighbors (KNN) algorithm can be used to build a loan approval prediction system. By properly preprocessing the data, scaling features, selecting the optimal K value, and evaluating performance using multiple metrics, the model can effectively classify whether a customer is likely to be approved for a personal loan.

The project serves as an excellent example of an end-to-end machine learning classification workflow using Python and Scikit-Learn.