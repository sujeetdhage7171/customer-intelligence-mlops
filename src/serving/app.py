from fastapi import FastAPI

from src.serving.schemas import IrisRequest
from src.serving.predictor import predict


app = FastAPI()


@app.get("/")
def health():

    return {"status": "healthy"}


@app.post("/predict")
def predict_api(request: IrisRequest):

    data = request.dict()

    prediction = predict(data)

    return {
        "prediction": prediction
    }