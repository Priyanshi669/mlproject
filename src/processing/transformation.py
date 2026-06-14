from src.config.constants import (
    FEATURE_COLUMNS,
    TARGET_COLUMN
)


class DataTransformation:

    def transform(self, df):
        df["Future_GHI"] = df["GHI"].shift(-1)

        df = df.dropna()

        X = df[FEATURE_COLUMNS].copy()

        y = df["Future_GHI"].copy()

        return X, y