import json
import pathlib as p
import joblib
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import roc_auc_score
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

RAW = p.Path("data/raw/telco_churn.csv")
ART = p.Path("artifacts")
ART.mkdir(exist_ok=True, parents=True)

df = pd.read_csv(RAW)

# Prepare target and features
y = (df["Churn"] == "Yes").astype(int)
X = df.drop(columns=["Churn", "customerID"])

# Identify numeric and categorical columns
num = X.select_dtypes(include="number").columns.tolist()
cat = [c for c in X.columns if c not in num]

# Create preprocessing pipeline
pre = ColumnTransformer([
    ("num", StandardScaler(), num),
    ("cat", OneHotEncoder(handle_unknown="ignore"), cat)
])

# Define model candidates
candidates = {
    "logreg": Pipeline([("pre", pre), ("clf", LogisticRegression(max_iter=500, class_weight="balanced"))]),
    "rf":     Pipeline([("pre", pre), ("clf", RandomForestClassifier(n_estimators=400, random_state=13))])
}

# Train/test split
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

# Train and evaluate models
best, best_auc = None, -1
for name, pipe in candidates.items():
    print(f"Training {name}...")
    pipe.fit(X_tr, y_tr)
    auc = roc_auc_score(y_te, pipe.predict_proba(X_te)[:, 1])
    print(f"{name} ROC AUC: {auc:.4f}")
    if auc > best_auc:
        best, best_auc = pipe, auc

# Save best model
joblib.dump(best, ART / "model.joblib")
(ART / "metrics.json").write_text(json.dumps({"roc_auc": float(best_auc)}, indent=2))

print(f"\nBest AUC: {best_auc:.4f}")
print(f"Model saved to {ART / 'model.joblib'}")
print(f"Metrics saved to {ART / 'metrics.json'}")

