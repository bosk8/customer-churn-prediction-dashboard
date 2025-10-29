## ADDED Requirements

### Requirement: Model Training Pipeline
The system SHALL train machine learning models to predict customer churn using the IBM Telco Customer Churn dataset. The training process SHALL evaluate multiple model candidates and select the best performer based on ROC AUC score.

#### Scenario: Successful model training with AUC ≥ 0.75
- **WHEN** the training script is executed with valid data
- **THEN** the script trains both LogisticRegression and RandomForestClassifier models
- **AND** evaluates each model using ROC AUC on a held-out test set
- **AND** selects the model with the highest ROC AUC
- **AND** saves the best model to `artifacts/model.joblib`
- **AND** saves the ROC AUC metric to `artifacts/metrics.json`
- **AND** the saved ROC AUC value is ≥ 0.75

#### Scenario: Data preprocessing and feature engineering
- **WHEN** raw data is loaded from `data/raw/telco_churn.csv`
- **THEN** the customerID column is dropped from features
- **AND** the Churn target variable is converted from Yes/No to 1/0
- **AND** numeric features are standardized using StandardScaler
- **AND** categorical features are encoded using OneHotEncoder with `handle_unknown="ignore"`
- **AND** preprocessing is applied consistently via a ColumnTransformer in a Pipeline

#### Scenario: Train/test split with stratification
- **WHEN** preparing data for training
- **THEN** the data is split into train (80%) and test (20%) sets
- **AND** the split is stratified by the target variable to maintain class balance
- **AND** a random_state of 42 is used for reproducibility

#### Scenario: Model candidate evaluation
- **WHEN** training models
- **THEN** LogisticRegression is trained with `max_iter=500` and `class_weight="balanced"`
- **AND** RandomForestClassifier is trained with `n_estimators=400` and `random_state=13`
- **AND** both models are evaluated on the same test set using ROC AUC
- **AND** the model with higher ROC AUC is selected as the best model

### Requirement: Model Artifact Persistence
The system SHALL persist trained models and evaluation metrics in a standardized format for later use by scoring and dashboard components.

#### Scenario: Model serialization
- **WHEN** a model training completes successfully
- **THEN** the best model pipeline (including preprocessing) is saved using joblib to `artifacts/model.joblib`
- **AND** the model can be loaded later using `joblib.load()` without errors

#### Scenario: Metrics serialization
- **WHEN** model evaluation completes
- **THEN** the ROC AUC score is saved as a JSON file at `artifacts/metrics.json`
- **AND** the JSON file contains a `roc_auc` field with the numeric score
- **AND** the JSON is formatted with indentation for readability
