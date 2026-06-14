from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
    mean_absolute_percentage_error
)


class ModelEvaluator:

    def evaluate(
        self,
        model,
        X_test,
        y_test
    ):

        predictions = model.predict(X_test)

        mae = mean_absolute_error(
            y_test,
            predictions
        )

        rmse = mean_squared_error(
            y_test,
            predictions,
            squared=False
        )

        mape = mean_absolute_percentage_error(
          y_test,
          predictions
      )

        r2 = r2_score(
            y_test,
            predictions
        )

        print("\nModel Performance")

        print(f"MAE  : {mae:.4f}")
        print(f"RMSE : {rmse:.4f}")
        print(f"R²   : {r2:.4f}")
        print(f"MAPE : {mape:.4f}")

        return {
            "mae": mae,
            "rmse": rmse,
            "r2": r2,
            "mape":mape,
        }