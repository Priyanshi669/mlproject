class DataTransformation:

    FEATURES = [
        "Temperature",
        "Clearsky GHI",
        "Clearsky DNI",
        "Clearsky DHI",
        "Month",
        "Day",
        "Hour"
    ]

    TARGET = "GHI"

    def transform(self, df):

        X = df[self.FEATURES]

        y = df[self.TARGET]

        return X, y