from unittest.mock import patch, MagicMock
from sklearn.pipeline import Pipeline
import pytest
import pandas as pd

from src.train import main
import src.train


@pytest.fixture
def mock_dependencies(monkeypatch):
    """
    Mock dependencies for the train script.
    """
    monkeypatch.setattr("src.train.load_data", MagicMock())
    monkeypatch.setattr(
        "src.train.prepare_data",
        MagicMock(return_value=(pd.DataFrame(), pd.Series()))
    )
    monkeypatch.setattr(
        "src.train.get_column_types",
        MagicMock(return_value=([], []))
    )
    monkeypatch.setattr("src.train.create_preprocessor", MagicMock())
    monkeypatch.setattr(
        "src.train.train_model",
        MagicMock(return_value=(MagicMock(spec=Pipeline), 0.85))
    )
    monkeypatch.setattr("src.train.save_artifacts", MagicMock())


def test_train_script(mock_dependencies):
    """
    Test that the train script runs without errors.
    """
    with patch("builtins.print"):
        main()

        # Check that the key functions are called
        src.train.load_data.assert_called_once()
        src.train.prepare_data.assert_called_once()
        src.train.get_column_types.assert_called_once()
        src.train.create_preprocessor.assert_called_once()
        src.train.train_model.assert_called_once()
        src.train.save_artifacts.assert_called_once()
