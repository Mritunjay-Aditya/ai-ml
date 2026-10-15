# Salary Prediction Using Simple Linear Regression

## Overview

This project uses **Simple Linear Regression** to predict a person's salary based on their years of work experience.

The dataset is downloaded directly from Kaggle using the `kagglehub` package and is used to train a machine learning model. After training, the program allows users to continuously enter years of experience and receive salary predictions until they type `exit`.

---

## Technologies Used

- Python
- Pandas
- Matplotlib
- Scikit-learn
- KaggleHub

---

## Dataset

Dataset: Salary Data

Features used:

| Column | Description |
|----------|-------------|
| Years of Experience | Input feature (Independent Variable) |
| Salary | Target variable (Dependent Variable) |

---

## Machine Learning Model

The project uses:

```python
LinearRegression()
```

Simple Linear Regression attempts to find the best-fit line:

```
Salary = m × Experience + c
```

Where:

- `m` = slope coefficient
- `c` = intercept

The model learns these values during training.

---

## Project Workflow

### Step 1: Download Dataset

The dataset is downloaded automatically from Kaggle.

```python
path = kagglehub.dataset_download(
    "mohithsairamreddy/salary-data"
)
```

---

### Step 2: Load Dataset

The CSV file is loaded into a Pandas DataFrame.

```python
data = pd.read_csv(csv_path)
```

Sample output:

| Years of Experience | Salary |
|---------------------|----------|
| 1.2 | 39344 |
| 1.5 | 46206 |
| 2.0 | 37732 |

---

### Step 3: Select Features

Input feature:

```python
X = data[["Years of Experience"]]
```

Target variable:

```python
y = data["Salary"]
```

---

### Step 4: Train-Test Split

The dataset is divided into:

- 80% Training Data
- 20% Testing Data

```python
train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
```

Purpose:

- Training data teaches the model.
- Testing data evaluates the model.

---

### Step 5: Train the Model

Create and train the linear regression model.

```python
model = LinearRegression()
model.fit(X_train, y_train)
```

The model learns the relationship between experience and salary.

---

### Step 6: Display Learned Equation

Extract model parameters:

```python
slope = model.coef_[0]
intercept = model.intercept_
```

Example:

```
Salary = 9449.96 × Experience + 25792.20
```

Meaning:

- Every additional year of experience increases salary by approximately ₹9,450.

---

### Step 7: Evaluate Model Performance

Predictions are generated on the test dataset.

```python
y_pred = model.predict(X_test)
```

Metrics used:

#### Mean Absolute Error (MAE)

```python
mean_absolute_error(y_test, y_pred)
```

Measures average prediction error.

---

#### Root Mean Squared Error (RMSE)

```python
mean_squared_error(y_test, y_pred) ** 0.5
```

Measures prediction accuracy while penalizing larger errors.

---

#### R² Score

```python
r2_score(y_test, y_pred)
```

Value range:

- 1.0 = Perfect prediction
- 0.0 = No correlation

Higher values indicate a better model.

---

### Step 8: Visualize Results

A scatter plot displays actual data points.

```python
plt.scatter(...)
```

A red line displays the regression line.

```python
plt.plot(...)
```

Graph Interpretation:

- Blue points = Actual salaries
- Red line = Predicted linear relationship

---

### Step 9: Continuous Salary Prediction

The program continuously accepts user input.

Example:

```text
Enter years of experience (or type 'exit' to quit): 5
Predicted salary for 5 years: ₹73,500

Enter years of experience (or type 'exit' to quit): 8
Predicted salary for 8 years: ₹101,850

Enter years of experience (or type 'exit' to quit): exit
Exiting program. Goodbye!
```

Implementation:

```python
while True:
```

Loop continues until:

```python
if user_input.lower() == "exit":
    break
```

---

## Input Validation

The program handles:

### Negative Values

```python
if years < 0:
```

Output:

```text
Experience cannot be negative.
```

---

### Invalid Data

```python
except ValueError:
```

Output:

```text
Invalid input. Please enter a valid number or 'exit'.
```

---

### Out-of-Range Predictions

If the entered experience is outside the dataset range:

```python
if years < minimum or years > maximum:
```

Output:

```text
Warning: This prediction is outside the dataset's experience range.
```

This is because the model is extrapolating beyond the training data.

---

## Advantages

- Simple and easy to understand.
- Demonstrates the complete machine learning workflow.
- Includes model evaluation.
- Provides data visualization.
- Handles invalid user inputs.
- Supports continuous predictions.

---

## Limitations

- Uses only one feature:
  - Years of Experience

Real salaries also depend on:

- Education
- Skills
- Company
- Location
- Industry
- Certifications

Adding more features would improve prediction accuracy.

---

## Future Improvements

Possible enhancements:

1. Multiple Linear Regression
2. Polynomial Regression
3. Save trained model using Pickle
4. Streamlit web application
5. GUI using Tkinter
6. Salary prediction API using Flask or FastAPI

---

## Conclusion

This project demonstrates how Simple Linear Regression can be used to predict salaries from years of experience. It covers data loading, preprocessing, model training, evaluation, visualization, and interactive salary prediction in a complete end-to-end machine learning workflow.