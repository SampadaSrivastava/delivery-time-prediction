from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI()

model = joblib.load("../model/model.pkl")
columns = joblib.load("../model/columns.pkl")

@app.post("/predict")
def predict(data: dict):
    input_data = [data.get(col, 0) for col in columns]
    prediction = model.predict([input_data])
    return {"predicted_delivery_time": float(prediction[0])}