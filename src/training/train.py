import mlflow
import mlflow.sklearn

import pandas as pd

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


# Create MLflow experiment
mlflow.set_experiment("customer-churn-prediction")


# Load sample dataset
data = load_iris()

X = data.data
y = data.target


# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Model parameters
max_depth = 5
random_state = 42


# Start MLflow run
with mlflow.start_run():

    # Log parameters
    mlflow.log_param("max_depth", max_depth)
    mlflow.log_param("random_state", random_state)

    # Create model
    model = RandomForestClassifier(
        max_depth=max_depth,
        random_state=random_state
    )

    # Train model
    model.fit(X_train, y_train)

    # Predict
    predictions = model.predict(X_test)

    # Evaluate
    accuracy = accuracy_score(y_test, predictions)

    # Log metric
    mlflow.log_metric("accuracy", accuracy)

    # Log model
    mlflow.sklearn.log_model(
        sk_model=model,
        name="customer_churn_model",
        registered_model_name="customer_churn_model"
    )

    print(f"Model Accuracy: {accuracy}")