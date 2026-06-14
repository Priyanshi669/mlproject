from xgboost import XGBRegressor


class ModelTrainer:

    def train(self, X_train, y_train):

        model = XGBRegressor(
            n_estimators=300,
            max_depth=6,
            learning_rate=0.05,
            objective="reg:squarederror",
            random_state=42
        )

        model.fit(X_train, y_train)

        return model