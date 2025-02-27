import joblib
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
model = joblib.load("model.pkl")
@app.get("/")
def home():
    return {"message": "Hello, FastAPI!"}

class InputData(BaseModel):
    feature1: float
    feature2: float

@app.post("/predict")
def predict(data: InputData):
    input_features = [[data.feature1, data.feature2]]
    prediction = model.predict(input_features)[0]
    return {"prediction": int(prediction)}
