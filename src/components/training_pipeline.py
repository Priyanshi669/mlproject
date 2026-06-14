from src.ingestion.solar_loader import SolarLoader
from src.components.data_validation import DataValidation

from src.processing.cleaning import DataCleaner
from src.processing.transformation import DataTransformation
from src.processing.feature_engineering import FeatureEngineer

from src.models.train import ModelTrainer
from src.models.evaluate import ModelEvaluator
from src.models.feature_importance import FeatureImportance

importance = FeatureImportance()


from src.storage.model_store import ModelStore

from src.config.paths import (
    DATA_PATH,
    MODEL_PATH
)


class TrainingPipeline:

    def run(self):

        # Load
        loader = SolarLoader()

        df = loader.load_data(DATA_PATH)
        for col in df.columns[:100]:
           print(col)
        # Validate
        validator = DataValidation()

        validator.validate(df)

        # Clean
        cleaner = DataCleaner()

        df = cleaner.clean(df)

        # Transform
        transformer = DataTransformation()

        X, y = transformer.transform(df)

        # Feature Engineering
        engineer = FeatureEngineer()

        X = engineer.engineer(X)

        # Time-Series Split
        split_idx = int(len(X) * 0.8)

        X_train = X.iloc[:split_idx]
        X_test = X.iloc[split_idx:]

        y_train = y.iloc[:split_idx]
        y_test = y.iloc[split_idx:]

        # Train
        trainer = ModelTrainer()

        model = trainer.train(
            X_train,
            y_train
        )
           
        # Evaluate
        evaluator = ModelEvaluator()

        evaluator.evaluate(
            model,
            X_test,
            y_test
        )
        importance.display(model)

        # Save
        store = ModelStore()

        store.save_model(
            model,
            MODEL_PATH
        )

        

if __name__ == "__main__":
    pipeline = TrainingPipeline()
    pipeline.run()        