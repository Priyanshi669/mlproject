import numpy as np
import pandas as pd


class DataCleaner:

    def clean(self, df: pd.DataFrame) -> pd.DataFrame:

        df = df.copy()

        print("\nStarting data cleaning...")

        # Replace invalid sensor values
        df.replace(-9999, np.nan, inplace=True)

        # Remove duplicates
        before = len(df)
        df.drop_duplicates(inplace=True)
        after = len(df)

        print(f"Removed {before - after} duplicate rows")

        # Fill numeric missing values
        numeric_cols = df.select_dtypes(include=["number"]).columns

        for col in numeric_cols:
            df[col] = df[col].fillna(df[col].median())

        print("Missing values handled")

        return df