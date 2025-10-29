import json
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
import joblib
from typing import Dict, Any

from src.config import CANDIDATES, MODEL_FILE, METRICS_FILE


def create_preprocessor(
    num_cols: list[str], cat_cols: list[str]
) -> ColumnTransformer:
    """
    Create the preprocessing pipeline.
    """
    return ColumnTransformer([
        ("num", StandardScaler(), num_cols),
        ("cat", OneHotEncoder(handle_unknown="ignore"), cat_cols)
    ])


def train_model(X, y, preprocessor):
    """
    Train and evaluate the model candidates.
    """
    X_tr, X_te, y_tr, y_te = train_test_split(
        X, y, test_size=0.2, stratify=y, random_state=42
    )

    best_model, best_auc = None, -1.0
    for name, clf in CANDIDATES.items():
        print(f"Training {name}...")
        pipe = Pipeline([("pre", preprocessor), ("clf", clf)])
        pipe.fit(X_tr, y_tr)
        auc = float(roc_auc_score(y_te, pipe.predict_proba(X_te)[:, 1]))
        print(f"{name} ROC AUC: {auc:.4f}")
        if auc > best_auc:
            best_model, best_auc = pipe, auc

    return best_model, best_auc


def save_artifacts(model, auc):
    """
    Save the model and metrics.
    """
    joblib.dump(model, MODEL_FILE)
    metrics: Dict[str, Any] = {"roc_auc": float(auc)}
    METRICS_FILE.write_text(json.dumps(metrics, indent=2))
