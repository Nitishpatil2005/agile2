import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def train_model(file_path):
    # Load CSV data
    df = pd.read_csv(file_path)

    # Debugging: Print first few rows
    print("Dataset Preview:\n", df.head())

    # Assuming first column as independent (X) and second column as dependent (Y)
    X = df.iloc[:, :-1].values  # All columns except last
    y = df.iloc[:, -1].values   # Only the last column

    # Debugging: Print shapes
    print("X shape:", X.shape)  # (rows, columns)
    print("y shape:", y.shape)  # (rows,)

    # Check if dimensions match
    if X.shape[0] != y.shape[0]:
        raise ValueError(f"Mismatch: X has {X.shape[0]} rows, y has {y.shape[0]} rows")

    # Split data into train & test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predictions
    y_pred = model.predict(X_test)

    # Debugging: Print shapes before plotting
    print("X_test shape:", X_test.shape)
    print("y_test shape:", y_test.shape)
    print("y_pred shape:", y_pred.shape)

    # Ensure X_test and y_test have the same number of points for plotting
    if X_test.shape[0] != y_test.shape[0]:
        raise ValueError("Mismatch between X_test and y_test sizes")

    # Plotting results
    plt.figure(figsize=(8, 5))
    plt.scatter(X_test, y_test, color='red', label="Actual")
    plt.plot(X_test, y_pred, color='blue', linewidth=2, label="Predicted")
    plt.xlabel("X values")
    plt.ylabel("Y values")
    plt.legend()
    plt.title("Linear Regression Results")
    plt.savefig("static/plot.png")  # Save plot to display in front-end

    # Return model accuracy
    accuracy = model.score(X_test, y_test)
    return accuracy
