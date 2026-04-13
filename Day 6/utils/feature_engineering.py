def create_features(temperature, humidity, usage_hours):

    error_count = 1 if temperature > 60 else 0
    vibration = 0.8 if temperature > 65 else 0.4

    avg_temp = temperature
    temp_change = temperature - 30

    usage_frequency = usage_hours / 24

    health_score = (
        100
        - temperature * 0.3
        - error_count * 5
        - vibration * 10
    )

    return [
        temperature,
        humidity,
        usage_hours,
        error_count,
        vibration,
        avg_temp,
        temp_change,
        usage_frequency,
        health_score
    ]