class DataValidation:

    def validate(self, df):

        print("=" * 50)

        print("Dataset Shape:")
        print(df.shape)

        print("\nMissing Values:")
        print(df.isnull().sum().sum())

        print("\nDuplicate Rows:")
        print(df.duplicated().sum())

        print("=" * 50)

        return True