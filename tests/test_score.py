from unittest.mock import patch, MagicMock
import pandas as pd
import numpy as np
import pytest
from pathlib import Path

from src.score import main
import src.score


@pytest.fixture
def mock_dependencies(monkeypatch):
    """
    Mock dependencies for the score script.
    """
    mock_model = MagicMock()
    mock_model.predict_proba.return_value = np.array([
        [0.1, 0.9], [0.2, 0.8], [0.3, 0.7], [0.4, 0.6]
    ])

    monkeypatch.setattr("src.score.joblib.load", MagicMock(return_value=mock_model))
    monkeypatch.setattr(
        "src.score.load_data",
        MagicMock(return_value=pd.DataFrame({
            "Churn": ["Yes", "No", "Yes", "No"],
            "customerID": ["1", "2", "3", "4"],
            "tenure": [1, 2, 3, 4],
            "MonthlyCharges": [10, 20, 30, 40]
        }))
    )

    # Mock the to_csv method on the DataFrame that will be created
    monkeypatch.setattr("pandas.DataFrame.to_csv", MagicMock())


def test_score_script(mock_dependencies):
    """
    Test that the score script runs without errors.
    """
    with patch("builtins.print"):
        main()

        # Check that the key functions are called
        src.score.joblib.load.assert_called_once()
        src.score.load_data.assert_called_once()

        # Check that the to_csv method was called with the correct arguments
        pd.DataFrame.to_csv.assert_called_once_with(
            Path("artifacts/top_risk.csv"), index=False
        )
