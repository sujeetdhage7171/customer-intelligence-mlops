import mlflow.pyfunc
import pandas as pd


#MODEL_URI = "models:/customer_churn_model/latest"
MODEL_URI = "/app/mlruns/1/models/m-9c3321fdfa044f4c970c321ab56becde/artifacts"


# Load latest registered model
model = mlflow.pyfunc.load_model(MODEL_URI)


def predict(data: dict):

    df = pd.DataFrame([data])

    prediction = model.predict(df)

    return prediction.tolist()