
from src.config.constants import FEATURE_COLUMNS


class FeatureImportance:

    def display(self, model):

        importance = model.feature_importances_

        results = sorted(
            zip(FEATURE_COLUMNS, importance),
            key=lambda x: x[1],
            reverse=True
        )

        print("\nFeature Importance")
        print("=" * 50)

        for feature, score in results:
            print(f"{feature:<20} {score:.4f}")

        return results