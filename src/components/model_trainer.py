from xgboost import XGBRegressor
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

import joblib
import os


class ModelTrainer:

    def train(self, X, y):

        split_idx = int(len(X) * 0.8)

        X_train = X.iloc[:split_idx]
        X_test = X.iloc[split_idx:]

        y_train = y.iloc[:split_idx]
        y_test = y.iloc[split_idx:]

        model = XGBRegressor(
            n_estimators=300,
            max_depth=6,
            learning_rate=0.05,
            objective="reg:squarederror"
        )

        model.fit(X_train, y_train)

        predictions = model.predict(X_test)

        print(
            "MAE:",
            mean_absolute_error(y_test, predictions)
        )

        print(
            "RMSE:",
            mean_squared_error(
                y_test,
                predictions,
                squared=False
            )
        )

        print(
            "R2:",
            r2_score(
                y_test,
                predictions
            )
        )

        os.makedirs(
            "artifacts",
            exist_ok=True
        )

        joblib.dump(
            model,
            "artifacts/solar_forecast_model.pkl"
        )

        return model