import kagglehub
import os
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)

# --------------------------------------------------
# 1. Download Dataset
# --------------------------------------------------
path = kagglehub.dataset_download(
    "mitgandhi10/dataset-for-random-forest-regression"
)

print("Dataset Path:")
print(path)

# --------------------------------------------------
# 2. Load Dataset
# --------------------------------------------------
csv_files = [
    file for file in os.listdir(path)
    if file.endswith(".csv")
]

if not csv_files:
    raise FileNotFoundError("No CSV file found in dataset directory.")

csv_path = os.path.join(path, csv_files[0])

data = pd.read_csv(csv_path)

# Remove extra spaces from column names
data.columns = data.columns.str.strip()

print("\nDataset Loaded Successfully!")
print("\nFirst 5 Records:")
print(data.head())

print("\nDataset Shape:", data.shape)
print("\nColumns:", data.columns.tolist())

# --------------------------------------------------
# 3. Remove Unnecessary Columns
# --------------------------------------------------
if "ID" in data.columns:
    data = data.drop(columns=["ID"])

# ZIP.Code is an identifier-like feature and can
# introduce misleading distance calculations in KNN.
if "ZIP.Code" in data.columns:
    data = data.drop(columns=["ZIP.Code"])

# --------------------------------------------------
# 4. Handle Missing Values
# --------------------------------------------------
data = data.dropna()

# --------------------------------------------------
# 5. Define Features and Target
# --------------------------------------------------
target = "Personal.Loan"

if target not in data.columns:
    raise ValueError(
        f"Target column '{target}' not found. "
        f"Available columns: {data.columns.tolist()}"
    )

X = data.drop(columns=[target])
y = data[target]

# Ensure all input features are numeric
X = X.apply(pd.to_numeric, errors="raise")

print("\nFeatures:")
print(X.columns.tolist())

print("\nTarget Distribution:")
print(y.value_counts())

# --------------------------------------------------
# 6. Train-Test Split
# --------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# --------------------------------------------------
# 7. Scale Features
# --------------------------------------------------
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# --------------------------------------------------
# 8. Find Best K Value
# --------------------------------------------------
accuracies = []

max_k = min(20, len(X_train))

for k in range(1, max_k + 1):

    knn = KNeighborsClassifier(n_neighbors=k)

    knn.fit(X_train_scaled, y_train)

    predictions = knn.predict(X_test_scaled)

    accuracy = accuracy_score(y_test, predictions)

    accuracies.append(accuracy)

best_k = accuracies.index(max(accuracies)) + 1

print("\nBest K =", best_k)
print("Best Accuracy =", round(max(accuracies), 4))

# --------------------------------------------------
# 9. Train Final Model
# --------------------------------------------------
model = KNeighborsClassifier(n_neighbors=best_k)

model.fit(X_train_scaled, y_train)

# --------------------------------------------------
# 10. Evaluate Model
# --------------------------------------------------
y_pred = model.predict(X_test_scaled)

print("\n----- MODEL EVALUATION -----")

print("\nAccuracy:")
print(round(accuracy_score(y_test, y_pred), 4))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred, zero_division=0))

# --------------------------------------------------
# 11. Plot Accuracy vs K
# --------------------------------------------------
plt.figure(figsize=(8, 5))

plt.plot(
    range(1, max_k + 1),
    accuracies,
    marker="o",
    color="blue"
)

plt.xlabel("K Value")
plt.ylabel("Accuracy")
plt.title("KNN: Accuracy vs K Value")
plt.xticks(range(1, max_k + 1))
plt.grid(True)
plt.tight_layout()
plt.show(block=False)

# --------------------------------------------------
# 12. Continuous Prediction System
# --------------------------------------------------
print("\n----------------------------")
print("LOAN APPROVAL PREDICTION")
print("Type 'exit' anytime to quit.")
print("----------------------------")

feature_names = X.columns.tolist()

while True:

    try:
        inputs = []

        for feature in feature_names:

            value = input(f"Enter {feature}: ").strip()

            if value.lower() == "exit":
                print("Program Terminated.")
                plt.close("all")
                raise SystemExit

            inputs.append(float(value))

        user_data = pd.DataFrame(
            [inputs],
            columns=feature_names
        )

        user_scaled = scaler.transform(user_data)

        prediction = model.predict(user_scaled)[0]

        probabilities = model.predict_proba(user_scaled)[0]

        print("\nPrediction Result:")

        if prediction == 1:
            print("Loan Approved")
        else:
            print("Loan Not Approved")

        print(
            f"Predicted Class Probability: "
            f"{max(probabilities) * 100:.2f}%"
        )

        print("-" * 40)

    except ValueError:
        print("\nInvalid input. Enter numeric values only.")