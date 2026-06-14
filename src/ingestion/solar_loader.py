import pandas as pd


class SolarLoader:

    def load_data(self, file_path):

        df = pd.read_csv(
            file_path,
            skiprows=2
        )

        return df