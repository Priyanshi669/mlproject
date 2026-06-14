import numpy as np


class FeatureEngineer:

    def engineer(self, X, df):

        X = X.copy()

        # Cyclic time
        X["hour_sin"] = np.sin(
            2 * np.pi * X["Hour"] / 24
        )

        X["hour_cos"] = np.cos(
            2 * np.pi * X["Hour"] / 24
        )

        # Previous hour irradiance
        X["ghi_lag_1"] = df["GHI"].shift(1)

        # Previous day same hour
        X["ghi_lag_24"] = df["GHI"].shift(24)

        return X