## ADDED Requirements

### Requirement: Artifact Directory Structure
The system SHALL maintain a dedicated `artifacts/` directory for storing model files, metrics, and output results.

#### Scenario: Artifact directory creation
- **WHEN** the training script executes
- **THEN** the `artifacts/` directory is created if it does not exist (with parent directories as needed)
- **AND** the directory structure supports storing multiple artifact types

### Requirement: Model Artifact Storage
The system SHALL persist trained machine learning models in a format that can be reliably loaded for scoring.

#### Scenario: Model file persistence
- **WHEN** a model training completes
- **THEN** the complete model pipeline (preprocessing + classifier) is saved to `artifacts/model.joblib`
- **AND** the file uses joblib serialization format
- **AND** the file can be loaded without requiring original training data or feature definitions

### Requirement: Metrics Storage
The system SHALL persist model evaluation metrics in a machine-readable format.

#### Scenario: Metrics JSON file
- **WHEN** model evaluation completes
- **THEN** a JSON file is created at `artifacts/metrics.json`
- **AND** the file contains a `roc_auc` field with the test set ROC AUC score as a float
- **AND** the JSON is formatted with 2-space indentation for readability
- **AND** the file can be parsed by standard JSON libraries

### Requirement: Prediction Result Export
The system SHALL export batch scoring results to a CSV file for consumption by the dashboard.

#### Scenario: Top risk CSV export
- **WHEN** batch scoring completes
- **THEN** a CSV file is created at `artifacts/top_risk.csv`
- **AND** the file contains columns: `customerID` and `churn_score`
- **AND** rows are sorted by `churn_score` in descending order
- **AND** the file contains the top 500 rows (or all rows if fewer than 500)
- **AND** the CSV excludes pandas index values in output
