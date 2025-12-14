import os
from typing import List

import joblib
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel

MODEL_VERSION = os.getenv("MODEL_VERSION", "v1.0.0")

CURRENT_DIR = os.path.dirname(__file__)

if MODEL_VERSION == "v1.1.0":
    model_filename = "model_v1_1.pkl"
else:
    model_filename = "model.pkl"

MODEL_PATH = os.path.join(CURRENT_DIR, model_filename)
model = joblib.load(MODEL_PATH)

app = FastAPI()


class PredictRequest(BaseModel):
    x: List[List[float]]


@app.get("/health")
def health():
    return {
        "status": "ok",
        "version": MODEL_VERSION
    }


@app.post("/predict")
def predict(request: PredictRequest):
    data = np.array(request.x)
    preds = model.predict(data).tolist()
    return {
        "version": MODEL_VERSION,
        "predictions": preds
    }
