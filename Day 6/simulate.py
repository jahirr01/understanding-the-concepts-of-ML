import requests
import time
import random

url = "http://127.0.0.1:8000/predict-device-status"

print("🚀 Starting IoT Simulation...\n")

while True:
    data = {
        "temperature": random.randint(25, 80),
        "humidity": random.randint(40, 90),
        "usage_hours": random.randint(1, 24)
    }

    response = requests.post(url, json=data)

    print("Input:", data)
    print("Prediction:", response.json())
    print("----------------------")

    time.sleep(2)