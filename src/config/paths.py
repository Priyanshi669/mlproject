from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent.parent

DATA_PATH = ROOT_DIR / "2016-190308-one_axis.csv"

MODEL_PATH = ROOT_DIR / "artifacts" / "solar_model.pkl"