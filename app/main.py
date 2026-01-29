import pickle
import pandas as pd
from fastapi import FastAPI
from app.schema import CustomerInput

app = FastAPI(
    title="Customer Churn Prediction API",
    description="Predicts probability of customer churn",
    version="1.0"
)

# Load model at startup
with open("model/churn_model.pkl", "rb") as f:
    model = pickle.load(f)

@app.post("/predict")
def predict_churn(customer: CustomerInput):
    data = pd.DataFrame([customer.dict()])

    churn_probability = model.predict_proba(data)[0][1]

    risk_level = "high" if churn_probability > 0.6 else "low"

    return {
        "churn_probability": round(float(churn_probability), 3),
        "risk_level": risk_level
    }

