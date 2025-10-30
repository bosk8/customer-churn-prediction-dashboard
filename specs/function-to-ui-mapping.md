# Function-to-UI Mapping

## Backend Features → UI Triggers & Data Contracts

This document maps backend functionality to UI components, data contracts, validations, error states, and feedback patterns.

---

## Feature 1: Model Training (`src/train.py`)

### Backend Functionality
- Loads raw CSV data (`data/raw/telco_churn.csv`)
- Preprocesses features (numeric standardization, categorical one-hot encoding)
- Trains multiple model candidates (Logistic Regression, Random Forest)
- Evaluates models using ROC AUC
- Saves best model to `artifacts/model.joblib`
- Saves metrics to `artifacts/metrics.json`

### UI Triggers
- **No direct UI trigger** (CLI-only operation)
- **Indirect UI impact**: Dashboard displays artifacts after training completes

### Data Contract (Input)
- **Input**: CSV file at `data/raw/telco_churn.csv`
- **Schema**: Must contain columns:
  - `customerID` (identifier, dropped)
  - `Churn` (target: "Yes"/"No")
  - Numeric features: `tenure`, `MonthlyCharges`, `TotalCharges`
  - Categorical features: 16 fields (see screens.md for full list)

### Data Contract (Output)
- **Output 1**: `artifacts/model.joblib`
  - Type: scikit-learn Pipeline object
  - Contains: Preprocessing transformers + trained classifier
  - Version: joblib format (compatible with scikit-learn version in requirements.txt)

- **Output 2**: `artifacts/metrics.json`
  - Schema: `{"roc_auc": <float>}`
  - Example: `{"roc_auc": 0.842}`
  - Type: JSON with float value

### Validations
- **File existence**: CSV must exist at specified path
- **Column presence**: Required columns must exist
- **Target encoding**: Churn column must contain "Yes"/"No" values
- **Data quality**: Missing values handled (StandardScaler for numeric, OneHotEncoder ignore for categorical)

### Error States
- **Missing CSV**: Script fails with FileNotFoundError → No UI impact (CLI error)
- **Invalid columns**: Script fails with KeyError → No UI impact (CLI error)
- **Training failure**: Script fails with sklearn error → No UI impact (CLI error)

### Feedback Patterns
- **CLI output**: Print statements to console
- **UI feedback**: Dashboard displays "AUC unavailable" if metrics.json missing

---

## Feature 2: Batch Scoring (`src/score.py`)

### Backend Functionality
- Loads trained model from `artifacts/model.joblib`
- Loads raw CSV data (`data/raw/telco_churn.csv`)
- Generates churn probabilities for all customers
- Sorts customers by churn_score descending
- Exports top 500 to `artifacts/top_risk.csv`

### UI Triggers
- **No direct UI trigger** (CLI-only operation)
- **Indirect UI impact**: Dashboard displays `top_risk.csv` table

### Data Contract (Input)
- **Input 1**: `artifacts/model.joblib` (required)
- **Input 2**: `data/raw/telco_churn.csv` (required)
  - Schema: Same as training input

### Data Contract (Output)
- **Output**: `artifacts/top_risk.csv`
  - Schema: `customerID,churn_score`
  - Format: CSV with header row
  - Rows: Exactly 500 (or fewer if dataset < 500 customers)
  - Sort: Descending by `churn_score`
  - Type: `churn_score` is float (0.0 to 1.0)

### Validations
- **Model existence**: Model file must exist (script fails if missing)
- **Data consistency**: CSV schema must match training data (same columns)
- **Row count**: Outputs min(500, dataset_size) rows

### Error States
- **Missing model**: Script fails with FileNotFoundError → Dashboard shows "Model artifact not found" in sidebar
- **Missing CSV**: Script fails with FileNotFoundError → No UI impact (CLI error)
- **Schema mismatch**: Script may fail or produce incorrect results → Dashboard displays data but may have issues

### Feedback Patterns
- **CLI output**: Print statement confirming file saved
- **UI feedback**: Dashboard displays error card if `top_risk.csv` missing

---

## Feature 3: Dashboard Display (Top 500 Table)

### Backend Functionality
- Reads `artifacts/top_risk.csv`
- Parses CSV into pandas DataFrame
- Displays in Streamlit dataframe component

### UI Triggers
- **Page load**: Automatic on dashboard initialization
- **Refresh**: Manual browser refresh or Streamlit rerun

### Data Contract (Input)
- **Input**: `artifacts/top_risk.csv`
  - Schema: `customerID` (string), `churn_score` (float)
  - Format: CSV with header row

### Data Contract (Output)
- **Output**: Streamlit dataframe component
  - Columns: customerID, churn_score
  - Rows: Up to 500 rows
  - Sort: User-configurable (default: churn_score descending)
  - Pagination: Streamlit native (100 rows per page default)

### Validations
- **File existence**: CSV must exist
- **File format**: Valid CSV with header row
- **Data types**: customerID (string), churn_score (numeric)

### Error States
- **Missing CSV**: Display error card: "Top risk CSV not found. Run scoring script first."
- **Invalid CSV**: Streamlit may show error → Catch exception, display error card
- **Empty CSV**: Display empty state message

### Feedback Patterns
- **Success**: Table displays with sortable columns
- **Error**: Error card with actionable message
- **Loading**: Streamlit spinner during file read

---

## Feature 4: Single-Customer Scoring (Form Submission)

### Backend Functionality
- Loads model from `artifacts/model.joblib` (on page load)
- Receives feature vector from form inputs
- Constructs feature DataFrame matching training schema
- Runs model.predict_proba() to get churn probability
- Returns probability value (0.0 to 1.0)

### UI Triggers
- **User action**: Click "SCORE CUSTOMER" button
- **Form validation**: Client-side validation must pass before submission

### Data Contract (Input)
- **Input**: Form data (19 features)
  - Numeric (3):
    - `tenure`: Integer (0-72)
    - `MonthlyCharges`: Float (0-200)
    - `TotalCharges`: Float (0-10000)
  - Categorical (16):
    - See screens.md for full list with options
  - Format: Dictionary or pandas DataFrame row

### Data Contract (Output)
- **Output**: Churn probability
  - Type: Float (0.0 to 1.0)
  - Format: Display as percentage (XX.X%)
  - Example: 0.653 → "65.3%"

### Validations

**Client-Side (Streamlit):**
- All fields required (enforced by Streamlit form)
- Numeric ranges: min/max values enforced by number_input
- Categorical options: Restricted to dropdown choices

**Server-Side (Model Pipeline):**
- Feature vector construction: Ensure all 19 features present
- Unknown categories: Handled by OneHotEncoder (handle_unknown="ignore")
- Missing values: Handled by StandardScaler (NaN → mean imputation implicit)
- Feature order: Must match training schema (column order)

### Error States
- **Missing model**: Form disabled, error message: "Model artifact not found. Run training script first."
- **Missing inputs**: Streamlit prevents submission (required field validation)
- **Invalid numeric range**: Streamlit number_input enforces min/max
- **Prediction failure**: Try/except catch → Display error card: "Prediction failed. Please check inputs and try again."
- **Schema mismatch**: Model pipeline may raise error → Display technical error message

### Feedback Patterns
- **Success**: Result card displays probability + risk badge + actionable text
- **Error**: Error card with message (inline below form)
- **Loading**: Submit button shows loading state (Streamlit native)
- **Validation**: Real-time feedback on invalid inputs (Streamlit native)

---

## Feature 5: Metrics Display (ROC AUC)

### Backend Functionality
- Reads `artifacts/metrics.json`
- Parses JSON to extract `roc_auc` value
- Displays in header card

### UI Triggers
- **Page load**: Automatic on dashboard initialization

### Data Contract (Input)
- **Input**: `artifacts/metrics.json`
  - Schema: `{"roc_auc": <float>}`
  - Type: JSON file

### Data Contract (Output)
- **Output**: Text display
  - Format: "ROC AUC: X.XXX" (3 decimal places)
  - Fallback: "AUC unavailable" if file missing

### Validations
- **File existence**: JSON file must exist
- **File format**: Valid JSON with `roc_auc` key
- **Value type**: `roc_auc` must be numeric (float)

### Error States
- **Missing file**: Display "AUC unavailable" (graceful degradation)
- **Invalid JSON**: Try/except catch → Display "AUC unavailable"
- **Missing key**: Try/except catch → Display "AUC unavailable"

### Feedback Patterns
- **Success**: Metric displays in header subtitle
- **Error**: Fallback text "AUC unavailable" (non-blocking)

---

## Data Flow Diagrams

### Flow 1: Dashboard Load
```
User opens dashboard
    ↓
Streamlit app initializes
    ↓
[Try] Load artifacts/metrics.json
    ├─ Success → Extract roc_auc → Display in header
    └─ Fail → Display "AUC unavailable"
    ↓
[Try] Load artifacts/top_risk.csv
    ├─ Success → Parse CSV → Display table
    └─ Fail → Display error card
    ↓
[Try] Load artifacts/model.joblib
    ├─ Success → Cache model object → Enable form
    └─ Fail → Disable form, show error message
```

### Flow 2: Form Submission
```
User fills form inputs
    ↓
User clicks "SCORE CUSTOMER"
    ↓
[Validate] Client-side validation (Streamlit)
    ├─ Fail → Display inline error, prevent submission
    └─ Pass → Continue
    ↓
[Construct] Feature vector from form data
    ├─ Numeric → StandardScaler transform (via model pipeline)
    ├─ Categorical → OneHotEncoder transform (via model pipeline)
    └─ Ensure column order matches training schema
    ↓
[Predict] model.predict_proba(feature_vector)[:, 1]
    ├─ Success → Extract probability (0.0-1.0)
    └─ Fail → Display error card
    ↓
[Display] Format probability + risk badge + actionable text
```

---

## Error Handling Strategy

### Error Hierarchy
1. **Critical errors**: Model missing, CSV missing → Disable functionality, show error card
2. **Non-critical errors**: Metrics missing → Graceful degradation, show fallback text
3. **Validation errors**: Invalid inputs → Inline feedback, prevent submission
4. **Runtime errors**: Prediction failure → Try/except catch, display error card

### Error Message Guidelines
- **Actionable**: Tell user what to do next
- **Technical (optional)**: For data scientists, include technical details
- **Consistent**: Use Bosk8 text-subtle color, meta-sm font size
- **Non-blocking**: Don't crash dashboard, allow partial functionality

### Error Recovery
- **User action**: Run training/scoring scripts → Refresh dashboard
- **Automatic**: Streamlit reruns on file changes (if watching filesystem)
- **Manual**: Browser refresh

---

## API Summary (Conceptual)

**Note:** This is not a REST API, but the functional interface between backend and UI.

| Function | Input | Output | Error Handling |
|----------|-------|--------|----------------|
| `load_metrics()` | None | `{"roc_auc": float}` or `None` | Returns `None` on error |
| `load_top_risk()` | None | `DataFrame` or `None` | Returns `None` on error, displays error card |
| `load_model()` | None | Pipeline object or `None` | Returns `None` on error, disables form |
| `score_customer(features)` | Dict of 19 features | Float (0.0-1.0) | Raises exception, caught by UI |
| `validate_features(features)` | Dict of features | Boolean | Client-side validation before submission |

