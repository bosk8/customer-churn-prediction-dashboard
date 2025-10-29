import pandas as pd
from typing import Tuple, List

from src.config import RAW_DATA


def load_data() -> pd.DataFrame:
    """
    Load the raw data from the specified path.
    """
    return pd.read_csv(RAW_DATA)


def prepare_data(df: pd.DataFrame) -> Tuple[pd.DataFrame, pd.Series]:
    """
    Prepare the data for training.
    """
    y = (df["Churn"] == "Yes").astype(int)
    X = df.drop(columns=["Churn", "customerID"])
    return X, y


def get_column_types(X: pd.DataFrame) -> Tuple[List[str], List[str]]:
    """
    Get the numeric and categorical column names.
    """
    num_cols = X.select_dtypes(include="number").columns.tolist()
    cat_cols = [c for c in X.columns if c not in num_cols]
    return num_cols, cat_cols
