# Information Architecture & User Flows

## Sitemap

**Single-Page Application Structure:**

```
Dashboard (streamlit_app.py)
├── Header Section
│   ├── Title Card (Hero)
│ده│   └── Metrics Display (ROC AUC)
│
├── Main Content Area
│   ├── Top 500 Risk Table
│   │   ├── Table Header (sortable)
│   │   ├── Data Rows (customerID, churn_score_html)
│   │   └── Export Controls (implicit via Streamlit)
│   │
│   └── Empty State (if CSV missing)
│
└── Sidebar
    ├── Single-Customer Form Section
    │   ├── Form Title
    │   ├── Input Fields (19 features)
    │   │   ├── Numeric Inputs (3)
    │   │   └── Categorical Selects (16)
    │   ├── Submit Button
    │   └── Result Display
    │       ├── Probability Metric
    │       └── Risk Badge
    │
    └── Error States (if model missing)
```

**Note:** Streamlit does not support true routing, so this is a virtual sitemap representing logical sections.

## User Flows

### Flow 1: Review Top At-Risk Customers (Happy Path)

```
[START] User opens dashboard URL
    │
    ├─► [LOAD] Dashboard initializes
    │   ├─► Load artifacts/metrics.json → Extract ROC AUC
    │   ├─► Load artifacts/top_risk.csv → DataFrame
    │   └─► Load artifacts/model.joblib → Model object
    │
    ├─► [RENDER] Header card displays
    │   ├─► Title: "CUSTOMER CHURN DASHBOARD"
    │   └─► Subtitle: "ROC AUC: 0.XXX" (or "AUC unavailable")
    │
    ├─► [RENDER] Main table displays
    │   ├─► Column headers: customerID | churn_score
    │   ├─► 500 rows (sorted desc by churn_score by default)
    │   └─► Streamlit native sorting enabled
    │
    ├─► [USER ACTION] User sorts table by customerID (optional)
    │
    ├─► [USER ACTION] User identifies high-risk customers
    │   └─► Mental threshold: churn_score > 0.7
    │
    ├─► [USER ACTION] User exports table (Streamlit download button)
    │   └─► CSV file downloads to local machine
    │
    └─► [END] User closes tab
```

**Edge Cases:**
- **CSV missing:** Display error card: "Top risk CSV not found. Run scoring script first."
- **Metrics missing:** Display "AUC unavailable" in header
- **Model missing:** Single-customer form disabled (graceful degradation)

### Flow 2: Single-Customer Scoring (Happy Path)

```
[START] User opens dashboard → Sidebar visible
    │
    ├─► [LOAD] Model loaded successfully (prerequisite check)
    │
    ├─► [RENDER] Form section displays
    │   ├─► Title: "SINGLE-CUSTOMER SCORING"
    │   └─► 19 input fields grouped by category
    │
    ├─► [USER INPUT] User fills form fields
    │   ├─► Numeric: Tenure (0-72), MonthlyCharges (0-200), TotalCharges (0-10000)
    │   ├─► Categorical: Gender (Male/Female), SeniorCitizen (Yes/No), etc.
    │   └─► Validation: Required fields enforced by Streamlit
    │
    ├─► [USER ACTION] User clicks "SCORE CUSTOMER" button
    │
    ├─► [VALIDATE] Client-side validation
    │   ├─► All fields filled? → Continue
    │   └─► Missing fields? → Display inline error, prevent submission
    │
    ├─► [PROCESS] Feature vector construction
    │   ├─► Extract numeric values → StandardScaler transform (via model pipeline)
    │   ├─► Extract categorical values → OneHotEncoder transform (via model pipeline)
    │   └─► Handle unknown categories (handle_unknown="ignore")
    │
    ├─► [PREDICT] Model inference
    │   ├─► model.predict_proba(feature_vector)[:, 1]
    │   └─► Returns probability: 0.0 to 1.0
    │
    ├─► [DISPLAY] Result card appears
    │   ├─► Probability: "XX.X%" (formatted to 1 decimal)
    │   ├─► Risk level badge:
    │   │   ├─► Low: 0-0.4 (green accent)
    │   │   ├─► Medium: 0.4-0.7 (text-muted)
    │   │   └─► High: 0.7-1.0 (text-primary, bold)
    │   └─► Actionable text: "Customer is at [LOW/MEDIUM/HIGH] risk of churning."
    │
    ├─► [USER ACTION] User adjusts inputs → Rescores (loop back to USER INPUT)
    │
    └─► [END] User satisfied with result
```

**Edge Cases:**
- **Model missing:** Form disabled, message: "Model artifact not found. Run training script first."
- **Invalid numeric input:** Streamlit handles (non-numeric → error, out of range → warning)
- **Unknown categorical value:** Model pipeline handles (OneHotEncoder ignore mode)
- **Prediction error:** Try/except → display error card with technical message
- **Empty form submission:** Streamlit prevents (required field validation)

### Flow 3: First-Time User / Empty State

```
[START] User opens dashboard (fresh deployment, no artifacts)
    │
    ├─► [CHECK] artifacts/metrics.json exists?
    │   ├─► No → Display "AUC unavailable" in header
    │   └─► Yes → Extract and display AUC
    │
    ├─► [CHECK] artifacts/top_risk.csv exists?
    │   ├─► No → Display error card:
    │   │   ├─► Title: "NO DATA AVAILABLE"
    │   │   ├─► Message: "Top risk CSV not found. Run scoring script first."
    │   │   └─► Action hint: "Run: python src/score.py"
    │   └─► Yes → Display table
    │
    ├─► [CHECK] artifacts/model.joblib exists?
    │   ├─► No → Sidebar form disabled, error message
    │   └─► Yes → Form enabled
    │
    └─► [END] User sees helpful error messages, knows next steps
```

### Flow 4: Error Recovery

```
[ERROR STATE] User sees error card (CSV/model missing)
    │
    ├─► [USER ACTION] User reads error message
    │
    ├─► [USER ACTION] User runs training/scoring scripts locally or via CLI
    │   ├─► python src/train.py
    │   └─► python src/score.py
    │
    ├─► [USER ACTION] User refreshes dashboard
    │
    ├─► [RECOVERY] Artifacts now present → Normal flow resumes
    │
    └─► [END] Dashboard functional
```

## Navigation Model

**Global Navigation:**
- None (single-page app)

**Secondary Navigation:**
- Scroll-based (main content → sidebar visible on right)
- Implicit sections:
  1. Header (top)
  2. Main table (center)
  3. Sidebar form (right, sticky on scroll)

**Breadcrumbs:**
- None (single-level hierarchy)

**Empty States:**
- **No CSV:** Error card in main area
- **No Model:** Error message in sidebar
- **No Metrics:** "AUC unavailable" text in header

**First-Run State:**
- All error cards visible with actionable hints
- User guided to run training/scoring scripts

## Route Rules

**N/A (Single-Page Application)**

Streamlit uses query parameters for state management, but no explicit routing. All functionality accessible on single page load.

## State Management

**Client-Side State (Streamlit Session State):**
- Form input values (persist on rerun)
- Last prediction result (cleared on new submission)
- Sort order (managed by Streamlit dataframe)

**Server-Side State:**
- Model object (loaded once, cached)
- CSV data (loaded once per page load, cached)
- Metrics JSON (loaded once per page load, cached)

**No Persistent State:**
- User preferences
- Historical predictions
- Custom thresholds

