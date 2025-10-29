## 1. Project Setup

- [x] 1.1 Create repository directory structure (data/raw, artifacts, app, src, notebooks, env)
- [x] 1.2 Create requirements.txt with all dependencies
- [x] 1.3 Create README.md with project documentation, metrics, and usage instructions
- [x] 1.4 Download IBM Telco Customer Churn dataset to data/raw/telco_churn.csv

## 2. Exploratory Data Analysis

- [x] 2.1 Create notebooks/01_eda.ipynb
- [x] 2.2 Inspect missing values and class balance
- [x] 2.3 Create basic univariate plots
- [x] 2.4 Perform target leakage checks
- [x] 2.5 Document categorical vs numeric columns

## 3. Model Training Implementation

- [x] 3.1 Implement src/train.py with data loading and preprocessing
- [x] 3.2 Implement ColumnTransformer with StandardScaler for numeric and OneHotEncoder for categorical features
- [x] 3.3 Implement model candidate evaluation (LogisticRegression and RandomForestClassifier)
- [x] 3.4 Add train/test split with stratification
- [x] 3.5 Implement ROC AUC evaluation metric
- [x] 3.6 Save best model to artifacts/model.joblib
- [x] 3.7 Save metrics to artifacts/metrics.json
- [ ] 3.8 Validate AUC ≥ 0.75; if not, tune model hyperparameters (requires dependency installation and execution)

## 4. Batch Scoring Implementation

- [x] 4.1 Implement src/score.py to load model and generate predictions
- [x] 4.2 Calculate churn probabilities for all customers
- [x] 4.3 Sort customers by churn score (descending)
- [x] 4.4 Export top 500 at-risk customers to artifacts/top_risk.csv

## 5. Streamlit Dashboard Implementation

- [x] 5.1 Implement app/streamlit_app.py with page configuration
- [x] 5.2 Create main view displaying top 500 at-risk customers table
- [x] 5.3 Implement sidebar for optional single-customer form
- [x] 5.4 Load and display model artifacts
- [x] 5.5 Add error handling for missing artifacts

## 6. Testing and Validation

- [ ] 6.1 Verify artifacts/model.joblib exists and is loadable (requires running train.py)
- [ ] 6.2 Verify artifacts/metrics.json contains ROC AUC ≥ 0.75 (requires running train.py)
- [ ] 6.3 Verify artifacts/top_risk.csv contains exactly 500 rows with customerID and churn_score (requires running score.py)
- [ ] 6.4 Test Streamlit app locally loads without errors (requires dependency installation)
- [ ] 6.5 Validate table renders correctly in dashboard (requires dependency installation and execution)

## 7. Deployment

- [ ] 7.1 Initialize git repository and make initial commit
- [ ] 7.2 Create at least 6 meaningful commits following project milestones
- [ ] 7.3 Push repository to GitHub (public recommended)
- [ ] 7.4 Deploy to Streamlit Community Cloud
- [ ] 7.5 Add deployment URL to README.md
- [ ] 7.6 Verify public app loads and displays correctly

## 8. Documentation

- [x] 8.1 Document feature engineering approach in README
- [x] 8.2 Document model performance metrics
- [x] 8.3 Add usage instructions for training and scoring scripts
- [x] 8.4 Add deployment instructions
- [x] 8.5 Document troubleshooting steps for common issues
