import pathlib as p
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

# Paths
RAW_DATA = p.Path("data/raw/telco_churn.csv")
ARTIFACTS = p.Path("artifacts")
MODEL_FILE = ARTIFACTS / "model.joblib"
METRICS_FILE = ARTIFACTS / "metrics.json"
TOP_RISK_FILE = ARTIFACTS / "top_risk.csv"

# Model candidates
CANDIDATES = {
    "logreg": LogisticRegression(
        max_iter=500, class_weight="balanced"
    ),
    "rf": RandomForestClassifier(
        n_estimators=400, random_state=13
    )
}
