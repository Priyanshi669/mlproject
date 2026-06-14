# src/models/predict.py

import joblib
import pandas as pd


class Predictor:

    def __init__(self, model_path):

        self.model = joblib.load(model_path)

    def predict(self, input_data):

        if isinstance(input_data, dict):

            input_data = pd.DataFrame([input_data])

        predictions = self.model.predict(input_data)

        return predictions