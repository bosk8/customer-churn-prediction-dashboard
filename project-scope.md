# Customer Churn Prediction Dashboard — Project Scope  
**Stack:** Python • scikit-learn • Streamlit • Machine Learning

## 0) Purpose
Predict customer churn and surface the **top 500 at-risk customers** in a live Streamlit app. End-to-end, reproducible, zero-context build.

## 1) Success Criteria
- Train/test split with **ROC AUC ≥ 0.75**.
- Saved model artifact + metrics JSON.
- Streamlit app deployed on Community Cloud and public.
- README documents features, metrics, and usage.

## 2) Scope and Non-Goals
- Scope: tabular ML on labeled churn dataset, minimal features, risk list UI.
- Non-Goals: deep learning, time-series survival analysis, PII ingestion.

## 3) Prereqs
- Python 3.10+, Git, GitHub account, Streamlit Community Cloud account.

## 4) Repository Layout
````

churn-streamlit/
├─ data/
│  └─ raw/telco_churn.csv
├─ artifacts/                    # model + outputs
├─ app/streamlit_app.py
├─ src/{train.py, score.py, utils.py}
├─ notebooks/01_eda.ipynb
├─ env/requirements.txt
└─ README.md

```

### env/requirements.txt
```

pandas>=2.2
numpy>=1.26
scikit-learn>=1.5
streamlit>=1.39
joblib>=1.4

````

## 5) Data
Use **IBM Telco Customer Churn** CSV (any mirror). Save to `data/raw/telco_churn.csv`.  
- Target: `Churn` in {Yes, No}.  
- Drop identifiers (`customerID`).  
- Convert Yes/No to 1/0 for target.

## 6) Build Steps

### 6.1 Create environment
```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r env/requirements.txt
````

### 6.2 EDA (notebook outline)

* Inspect missing values, class balance.
* Basic univariate plots, target leakage checks.
* Note categorical vs numeric columns.

### 6.3 Training script (`src/train.py`)

```python
import json, pathlib as p, joblib
import pandas as pd, numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import roc_auc_score
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

RAW = p.Path("data/raw/telco_churn.csv")
ART = p.Path("artifacts"); ART.mkdir(exist_ok=True, parents=True)
df = pd.read_csv(RAW)

y = (df["Churn"]=="Yes").astype(int)
X = df.drop(columns=["Churn","customerID"])

num = X.select_dtypes(include="number").columns.tolist()
cat = [c for c in X.columns if c not in num]

pre = ColumnTransformer([
  ("num", StandardScaler(), num),
  ("cat", OneHotEncoder(handle_unknown="ignore"), cat)
])

candidates = {
  "logreg": Pipeline([("pre", pre), ("clf", LogisticRegression(max_iter=500, class_weight="balanced"))]),
  "rf":     Pipeline([("pre", pre), ("clf", RandomForestClassifier(n_estimators=400, random_state=13))])
}

X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

best, best_auc = None, -1
for name, pipe in candidates.items():
    pipe.fit(X_tr, y_tr)
    auc = roc_auc_score(y_te, pipe.predict_proba(X_te)[:,1])
    if auc > best_auc:
        best, best_auc = pipe, auc

joblib.dump(best, ART/"model.joblib")
(ART/"metrics.json").write_text(json.dumps({"roc_auc": float(best_auc)}, indent=2))
print("Best AUC:", best_auc)
```

### 6.4 Batch scoring (`src/score.py`)

```python
import pandas as pd, joblib
df = pd.read_csv("data/raw/telco_churn.csv")
model = joblib.load("artifacts/model.joblib")
scores = model.predict_proba(df.drop(columns=["Churn","customerID"]))[:,1]
out = df.assign(churn_score=scores).sort_values("churn_score", ascending=False)
out[["customerID","churn_score"]].head(500).to_csv("artifacts/top_risk.csv", index=False)
```

### 6.5 Streamlit app (`app/streamlit_app.py`)

```python
import streamlit as st, pandas as pd, joblib

st.set_page_config(page_title="Churn Predictor", layout="wide")
st.title("Customer Churn Prediction")

model = joblib.load("artifacts/model.joblib")

st.header("Top 500 at-risk customers")
df = pd.read_csv("artifacts/top_risk.csv")
st.dataframe(df.head(500))

st.sidebar.header("Single-customer form (optional)")
st.sidebar.caption("Build inputs to score a hypothetical customer.")
# Example: collect a few fields and create a one-row DataFrame to score
# proba = model.predict_proba(row_df)[:,1][0]
# st.metric("Churn probability", f"{proba:.1%}")
```

### 6.6 Run locally

```bash
python src/train.py
python src/score.py
streamlit run app/streamlit_app.py
```

## 7) Deploy to Streamlit Community Cloud

* Push to GitHub (public recommended).
* In Streamlit Cloud: **Create app** → repo + `app/streamlit_app.py` → Deploy.
* Add the URL to README.

## 8) QA

* Verify `artifacts/model.joblib`, `artifacts/metrics.json`, `artifacts/top_risk.csv`.
* Confirm AUC ≥ 0.75; if not, tune features or model.
* App loads without errors; table renders.

## 9) Deliverables

* Code, artifacts, public app URL, README with metrics and instructions.
* ≥6 meaningful commits with messages tied to changes.

## 10) Troubleshooting

* Categorical parsing errors → cast strings; avoid mixed types.
* Poor AUC → add interactions, tune RF depth/trees, or calibrate threshold.

````
