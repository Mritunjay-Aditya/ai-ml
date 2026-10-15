import kagglehub
import os
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# 1. Download the dataset
path = kagglehub.dataset_download("mohithsairamreddy/salary-data")

# 2. Load the CSV file
csv_path = os.path.join(path, "Salary_Data.csv")
data = pd.read_csv(csv_path)

print("Dataset loaded successfully!")
print("Total records:", len(data))
print(data.head())

# 3. Select input and target columns
data = data[["Years of Experience", "Salary"]].dropna()

X = data[["Years of Experience"]]
y = data["Salary"]

# 4. Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 5. Train model
model = LinearRegression()
model.fit(X_train, y_train)

# 6. Display equation
slope = model.coef_[0]
intercept = model.intercept_

print("\n--- Trained Linear Regression Model ---")
print(f"Equation: Salary = {slope:.2f} × Experience + {intercept:.2f}")

# 7. Evaluate model
y_pred = model.predict(X_test)

print("\n--- Model Evaluation ---")
print(f"Mean Absolute Error: {mean_absolute_error(y_test, y_pred):.2f}")
print(f"Root Mean Squared Error: {mean_squared_error(y_test, y_pred) ** 0.5:.2f}")
print(f"R-squared Score: {r2_score(y_test, y_pred):.4f}")

# 8. Plot graph BEFORE entering prediction loop
plot_data = data.sort_values("Years of Experience")

plt.figure(figsize=(8, 5))

plt.scatter(
    X["Years of Experience"],
    y,
    color="blue",
    alpha=0.5,
    label="Actual Data"
)

plt.plot(
    plot_data["Years of Experience"],
    model.predict(plot_data[["Years of Experience"]]),
    color="red",
    linewidth=2,
    label="Regression Line"
)

plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.title("Salary Prediction Using Linear Regression")
plt.legend()
plt.grid(True)

# Non-blocking display
plt.show(block=False)

# 9. Continuous prediction loop
minimum = X["Years of Experience"].min()
maximum = X["Years of Experience"].max()

while True:
    user_input = input(
        "\nEnter years of experience (or type 'exit' to quit): "
    )

    if user_input.lower() == "exit":
        print("Exiting program. Goodbye!")
        break

    try:
        years = float(user_input)

        if years < 0:
            print("Experience cannot be negative.")
            continue

        new_data = pd.DataFrame(
            {"Years of Experience": [years]}
        )

        predicted_salary = model.predict(new_data)[0]

        print(
            f"Predicted salary for {years:g} years: ₹{predicted_salary:,.2f}"
        )

        if years < minimum or years > maximum:
            print(
                "Warning: This prediction is outside the dataset's experience range."
            )

    except ValueError:
        print(
            "Invalid input. Please enter a valid number or 'exit'."
        )
