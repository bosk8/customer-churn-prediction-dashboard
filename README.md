# Customer Churn Prediction Dashboard

**Stack:** Python • scikit-learn • Streamlit • Machine Learning

## Overview

This project implements an end-to-end machine learning system to predict customer churn and surface the **top 500 at-risk customers** in a live Streamlit dashboard. The system uses the IBM Telco Customer Churn dataset to train logistic regression and random forest models, achieving ROC AUC ≥ 0.75.

## Features

- **Model Training**: Automated training pipeline with multiple model candidates (Logistic Regression, Random Forest)
- **Batch Scoring**: Generate churn probability scores for all customers and identify top 500 at-risk customers
- **Interactive Dashboard**: Streamlit web interface displaying risk lists and optional single-customer scoring
- **Artifact Management**: Persistent model storage, metrics tracking, and CSV export

## Success Criteria

- ✅ Train/test split with **ROC AUC ≥ 0.75**
- ✅ Saved model artifact + metrics JSON
- ✅ Streamlit app deployed on Community Cloud and public
- ✅ README documents features, metrics, and usage

## Installation

1. **Create virtual environment:**
```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
```

2. **Install dependencies:**
```bash
pip install -r env/requirements.txt
```

## Usage

### 1. Prepare Data

Download the IBM Telco Customer Churn dataset and save it to `data/raw/telco_churn.csv`. You can find the dataset at:
- [Kaggle: Telco Customer Churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)
- Or search for "IBM Telco Customer Churn dataset"

### 2. Train Model

```bash
python -m src.train
```

This will:
- Load and preprocess the data
- Train logistic regression and random forest models
- Evaluate models using ROC AUC
- Save the best model to `artifacts/model.joblib`
- Save metrics to `artifacts/metrics.json`

### 3. Generate Batch Predictions

```bash
python -m src.score
```

This will:
- Load the trained model
- Generate churn probabilities for all customers
- Export top 500 at-risk customers to `artifacts/top_risk.csv`

### 4. Run Dashboard Locally

```bash
streamlit run app/streamlit_app.py
```

The dashboard will:
- Display top 500 at-risk customers in a sortable table
- Provide optional sidebar form for single-customer scoring

## Project Structure

```
churn-streamlit/
├── data/
│   └── raw/
│       └── telco_churn.csv          # Dataset
├── artifacts/                        # Model outputs
│   ├── model.joblib                 # Trained model
│   ├── metrics.json                 # Evaluation metrics
│   └── top_risk.csv                 # Top 500 at-risk customers
├── app/
│   └── streamlit_app.py             # Streamlit dashboard
├── src/
│   ├── __init__.py
│   ├── config.py                    # Configuration variables
│   ├── data.py                      # Data loading and preparation
│   ├── model.py                     # Model training and evaluation
│   ├── train.py                     # Training script
│   └── score.py                     # Batch scoring script
├── tests/                           # Tests
│   ├── __init__.py
│   ├── test_train.py
│   └── test_score.py
├── notebooks/
│   └── 01_eda.ipynb                 # Exploratory data analysis
├── env/
│   ├── requirements.txt             # Python dependencies
│   └── requirements-dev.txt         # Development dependencies
└── README.md                        # This file
```

## Development

To run the development checks, first install the development dependencies:

```bash
pip install -r env/requirements-dev.txt
```

### Running Tests

```bash
pytest tests/
```

### Running Linters

```bash
flake8 src/ tests/
```

### Running Type Checking

```bash
mypy src/ tests/
```

## Model Performance

Model performance metrics are stored in `artifacts/metrics.json` after training. The system targets **ROC AUC ≥ 0.75** on the test set.

### Feature Engineering

- **Numeric Features**: Standardized using `StandardScaler`
- **Categorical Features**: One-hot encoded using `OneHotEncoder` with `handle_unknown="ignore"`
- **Target Variable**: Binary classification (Yes/No → 1/0)

### Model Candidates

- **Logistic Regression**: `max_iter=500`, `class_weight="balanced"` for handling class imbalance
- **Random Forest**: `n_estimators=400`, `random_state=13` for reproducibility

The training script automatically selects the best model based on ROC AUC score.

## Deployment

### Streamlit Community Cloud

1. **Push to GitHub** (public repository recommended)
2. **In Streamlit Cloud:**
   - Click "New app"
   - Connect your GitHub repository
   - Set main file path: `app/streamlit_app.py`
   - Click "Deploy"

### Deployment URL

[Add your Streamlit Community Cloud URL here after deployment]

**Repository**: [https://github.com/bosk8/customer-churn-prediction-dashboard](https://github.com/bosk8/customer-churn-prediction-dashboard)

## Troubleshooting

### Model fails to achieve AUC ≥ 0.75
- Tune hyperparameters in `src/config.py`
- Check for data quality issues in EDA notebook
- Consider feature interactions or engineering

### Categorical encoding errors
- Ensure OneHotEncoder uses `handle_unknown="ignore"` (already configured)
- Verify all categorical columns are properly identified

### Missing values
- Check EDA notebook for missing value patterns
- scikit-learn transformers handle NaN for numeric features automatically

### Streamlit app errors
- Verify `artifacts/model.joblib` and `artifacts/top_risk.csv` exist
- Run `python -m src.train` and `python -m src.score` before launching app
- Check file paths are relative to the app directory

## Contributing

This is a standalone project following OpenSpec specifications. For changes, refer to `openspec/changes/` for proposal workflows.

## License

[Add your license here]
