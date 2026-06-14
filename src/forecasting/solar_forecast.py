# src/forecasting/solar_forecast.py

from src.models.predict import Predictor
from src.config.paths import MODEL_PATH


class SolarForecaster:

    def __init__(self):

        self.predictor = Predictor(MODEL_PATH)

    def forecast(
        self,
        temperature,
        clearsky_ghi,
        clearsky_dni,
        clearsky_dhi,
        month,
        day,
        hour
    ):

        payload = {
            "Temperature": temperature,
            "Clearsky GHI": clearsky_ghi,
            "Clearsky DNI": clearsky_dni,
            "Clearsky DHI": clearsky_dhi,
            "Month": month,
            "Day": day,
            "Hour": hour
        }

        prediction = self.predictor.predict(payload)

        return {
            "predicted_ghi": float(prediction[0])
        }