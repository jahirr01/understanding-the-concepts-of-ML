from fastapi import FastAPI, HTTPException
import numpy as np
import pickle
import logging
from utils.feature_engineering import create_features

#  Logging setup
logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

app = FastAPI()

# Load model
with open("model/rf_model.pkl", "rb") as f:
    model = pickle.load(f)

@app.get("/")
def home():
    return {"message": "IoT ML API Running "}

@app.post("/predict-device-status")
def predict_device_status(data: dict):
    try:
        logging.info("Request received")

        # Validation
        if "temperature" not in data or "humidity" not in data or "usage_hours" not in data:
            raise HTTPException(status_code=400, detail="Missing required fields")

        temperature = data["temperature"]
        humidity = data["humidity"]
        usage_hours = data["usage_hours"]

        if temperature < 0 or humidity < 0 or usage_hours < 0:
            raise HTTPException(status_code=400, detail="Invalid input values")

        # Feature Engineering
        features = create_features(temperature, humidity, usage_hours)
        input_data = np.array([features])

        # Prediction
        prediction = model.predict(input_data)[0]

        logging.info(f"Prediction: {prediction}")

        return {"status": prediction}

    except Exception as e:
        logging.error(f"Error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))