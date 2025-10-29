## ADDED Requirements

### Requirement: Top Risk Customers Display
The system SHALL provide a Streamlit web interface that displays the top 500 at-risk customers in a tabular format.

#### Scenario: Dashboard initialization and layout
- **WHEN** the Streamlit app is launched
- **THEN** the page is configured with title "Churn Predictor" and wide layout
- **AND** a main title "Customer Churn Prediction" is displayed
- **AND** the app loads the model artifact from `artifacts/model.joblib`
- **AND** the top risk CSV is loaded from `artifacts/top_risk.csv`

#### Scenario: Display top 500 at-risk customers table
- **WHEN** the dashboard loads successfully
- **THEN** a header "Top 500 at-risk customers" is displayed
- **AND** a data table shows all rows from `artifacts/top_risk.csv` (up to 500 rows)
- **AND** the table displays `customerID` and `churn_score` columns
- **AND** the data table is sortable and searchable using Streamlit's dataframe features

### Requirement: Optional Single-Customer Scoring Form
The system SHALL provide an optional sidebar form for scoring individual hypothetical customers (implementation may be simplified or placeholder).

#### Scenario: Sidebar form structure
- **WHEN** the dashboard loads
- **THEN** a sidebar section titled "Single-customer form (optional)" is displayed
- **AND** a caption explains the form is for scoring hypothetical customers
- **AND** the form provides inputs to collect customer feature values
- **AND** when submitted, a churn probability is calculated and displayed as a metric

#### Scenario: Single-customer prediction display
- **WHEN** a user submits the single-customer form with valid feature values
- **THEN** the input features are converted to a DataFrame matching training data format
- **AND** the model's `predict_proba()` method is called on the DataFrame
- **AND** the churn probability is extracted and displayed as a formatted metric (e.g., "Churn probability: 23.5%")
