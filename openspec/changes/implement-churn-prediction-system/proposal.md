## Why

Build an end-to-end machine learning system to predict customer churn and surface at-risk customers in a production-ready Streamlit dashboard. This proposal implements the complete ML pipeline from data ingestion through model training, batch scoring, and interactive visualization.

## What Changes

- **ADDED**: Model training capability with logistic regression and random forest classifiers, achieving ROC AUC ≥ 0.75
- **ADDED**: Batch scoring capability to generate top 500 at-risk customer predictions
- **ADDED**: Streamlit dashboard for displaying risk lists and optional single-customer scoring
- **ADDED**: Artifact management for model persistence, metrics storage, and result export
- **ADDED**: Repository structure with proper separation of data, source code, artifacts, and application code

## Impact

- **Affected specs**: New capabilities for `model-training`, `batch-scoring`, `streamlit-dashboard`, and `artifact-management`
- **Affected code**: 
  - New files: `src/train.py`, `src/score.py`, `src/utils.py`, `app/streamlit_app.py`
  - New directories: `data/raw/`, `artifacts/`, `notebooks/`, `env/`
  - Configuration: `env/requirements.txt`, `README.md`
- **Dependencies**: pandas, numpy, scikit-learn, streamlit, joblib
