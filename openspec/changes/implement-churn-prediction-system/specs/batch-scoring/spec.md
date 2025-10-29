## ADDED Requirements

### Requirement: Batch Churn Prediction
The system SHALL generate churn probability scores for all customers in the dataset and identify the top 500 highest-risk customers.

#### Scenario: Generate predictions for all customers
- **WHEN** the scoring script is executed after model training
- **THEN** the script loads the trained model from `artifacts/model.joblib`
- **AND** loads the full dataset from `data/raw/telco_churn.csv`
- **AND** generates churn probability scores for all customers using `predict_proba()`
- **AND** extracts the probability of churn (class 1) for each customer

#### Scenario: Export top 500 at-risk customers
- **WHEN** churn scores are calculated for all customers
- **THEN** customers are sorted by churn score in descending order (highest risk first)
- **AND** the top 500 customers are selected
- **AND** a CSV file is created at `artifacts/top_risk.csv` containing `customerID` and `churn_score` columns
- **AND** the CSV file contains exactly 500 rows (or fewer if dataset has fewer than 500 customers)
- **AND** the CSV file excludes the index column

### Requirement: Scoring Consistency
The system SHALL ensure that scoring uses the same preprocessing pipeline as training to maintain consistency.

#### Scenario: Preprocessing consistency
- **WHEN** generating predictions
- **THEN** the loaded model pipeline includes both preprocessing and classification steps
- **AND** raw features are passed to the pipeline's `predict_proba()` method
- **AND** preprocessing is applied automatically by the pipeline without manual intervention
