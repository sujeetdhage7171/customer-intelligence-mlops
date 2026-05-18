import mlflow.pyfunc
import pandas as pd


MODEL_URI = "models:/customer_churn_model/latest"


# Load latest registered model
model = mlflow.pyfunc.load_model(MODEL_URI)


def predict(data: dict):

    df = pd.DataFrame([data])

    prediction = model.predict(df)

    return prediction.tolist()