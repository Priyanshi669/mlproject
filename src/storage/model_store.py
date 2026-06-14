import joblib
import os


class ModelStore:

    def save_model(
        self,
        model,
        path
    ):

        os.makedirs(
            os.path.dirname(path),
            exist_ok=True
        )

        joblib.dump(
            model,
            path
        )

        print(f"Model saved at {path}")