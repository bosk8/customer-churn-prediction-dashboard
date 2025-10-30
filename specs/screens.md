# Screen-by-Screen Specifications

## Screen 1: Main Dashboard

### Purpose
Primary landing view displaying model performance metrics, top 500 at-risk customers table, and access to single-customer scoring form.

### Wireframe (Text-Based)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           BOSK8 DASHBOARD                                   │
│                                                                             │
│  ┌──────────────────────────────────────────────────────────────────────┐  │
│  │                                                                      │  │
│  │  ┌──────────────────────────────────────────────────────────────┐   │  │
│  │  │                                                              │   │  │
│  │  │        CUSTOMER CHURN DASHBOARD                              │   │  │
│  │  │                                                              │   │  │
│  │  │        ROC AUC: 0.842                                       │   │  │
│  │  │                                                              │   │  │
│  │  └──────────────────────────────────────────────────────────────┘   │  │
│  │                              │                                       │  │
│  │  ┌──────────────────────────────────────────────────────────────┐   │  │
│  │  │ TOP 500 AT-RISK CUSTOMERS                                    │   │  │
│  │  ├──────────────────────┬──────────────────────────────────────┤   │  │
│  │  │ customerID           │ churn_score                          │   │  │
│  │  ├──────────────────────┼──────────────────────────────────────┤   │  │
│  │  │ 7590-VHVEG           │ 0.987                                │   │  │
│  │  │ 2234-XADUH           │ 0.965                                │   │  │
│  │  │ ...                  │ ...                                  │   │  │
│  │  │ [500 rows, sortable] │                                      │   │  │
│  │  └──────────────────────┴──────────────────────────────────────┘   │  │
│  │                                                                      │  │
│  └──────────────────────────────────────────────────────────────────────┘  │
│                                                                             │
│                        [SIDEBAR ON RIGHT - SEE SCREEN 2]                    │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Layout Grid

**Container:**
- Max width: `min(1100px, 90vw)` (style.md: `layout.containerMax`)
- Padding: `var(--space-4)` top, `var(--space-1)` sides/bottom
- Background: `var(--bg-elev1)`

**Header Card:**
- Width: 100% of container
- Padding: `var(--space-4)` (2rem) vertical, `var(--space-2)` (2rem) horizontal
- Border: Bottom only (`border-b` class)
- Background: `var(--surface-card)`
- Shadow: `box-shadow: 0 0 0 var(--border-outer-w) var(--border-color), 0 1px 2px var(--shadow-tint)`

**Table Card:**
- Width: 100% of container
- Padding: `var(--space-1)` (1rem)
- Border: Bottom only (`border-b` class)
- Background: `var(--surface-card)`

### Components

1. **Header Card (`metrics-card`)**
   - Title: "CUSTOMER CHURN DASHBOARD" (tagline class)
   - Subtitle: "ROC AUC: X.XXX" (meta-sm class) or "AUC unavailable"
   - Alignment: Center (flex column, items-center)
   - Gap: `var(--space-0_5)` between title and subtitle

2. **Table Container (`table-card`)**
   - Label: "TOP 500 AT-RISK CUSTOMERS" (meta-md class, uppercase)
   - Streamlit dataframe component (native)
   - Columns: `customerID`, `churn_score`
   - Default sort: Descending by `churn_score`
   - Pagination: Streamlit native (100 rows per page default)

3. **Error State Card (`error-card`)**
   - Padding: `var(--space-1)`
   - Background: `var(--surface-card)`
   - Text: `var(--text-subtle)`, `meta-sm` class
   - Message: "Top risk CSV not found. Run scoring script first."

### Responsive Rules

**Mobile (< 768px):**
- Container padding: `var(--space-1)` (reduced from 4rem)
- Header card padding: `var(--space-2)` vertical, `var(--space-1)` horizontal
- Table: Horizontal scroll enabled (Streamlit native)
- Sidebar: Hidden by default (Streamlit collapse)

**Tablet (768px - 1023px):**
- Container padding: `var(--space-2)` top
- Table: Full width, no horizontal scroll
- Sidebar: Visible, collapsible

**Desktop (≥ 1024px):**
- Border widths: `var(--border-w)` = 1.5px, `var(--border-outer-w)` = 2px
- Full layout: Header + table + sidebar all visible

### States

**Default State:**
- Header card displays with AUC metric
- Table displays 500 rows, sorted by churn_score descending
- Sidebar visible (desktop) or hidden (mobile)

**Loading State:**
- Streamlit shows spinner during artifact loading
- No custom skeleton loader (Bosk8 minimal aesthetic)

**Error State (CSV Missing):**
- Error card replaces table inner content
- Message: "Top risk CSV not found. Run scoring script first."
- Header card still displays (with "AUC unavailable" if metrics missing)

**Error State (Metrics Missing):**
- Header card displays "AUC unavailable" subtitle
- Table still displays if CSV exists

**Empty State (No Artifacts):**
- Header: "AUC unavailable"
- Table: Error card
- Sidebar: Error message

## Screen 2: Sidebar Form

### Purpose
Secondary interface for single-customer churn probability scoring via interactive form inputs.

### Wireframe (Text-Based)

```
┌─────────────────────────────────────┐
│  ┌───────────────────────────────┐  │
│  │ SINGLE-CUSTOMER SCORING       │  │
│  ├───────────────────────────────┤  │
│  │                               │  │
│  │ Gender                        │  │
│  │ [Male ▼]                      │  │
│  │                               │  │
│  │ SeniorCitizen                 │  │
│  │ [No ▼]                        │  │
│  │                               │  │
│  │ Partner                       │  │
│  │ [Yes ▼]                       │  │
│  │                               │  │
│  │ ... (16 more categorical)     │  │
│  │                               │  │
│  │ Tenure (months)               │  │
│  │ [0────72]                     │  │
│  │                               │  │
│  │ MonthlyCharges                │  │
│  │ [0────200]                    │  │
│  │                               │  │
│  │ TotalCharges                  │  │
│  │ [0────10000]                  │  │
│  │                               │  │
│  │ [SCORE CUSTOMER]              │  │
│  │                               │  │
│  │ ┌───────────────────────────┐ │  │
│  │ │ RESULT                    │ │  │
│  │ │                           │ │  │
│  │ │ Churn Probability: 65.3%  │ │  │
│  │ │                           │ │  │
│  │ │ [HIGH RISK]               │ │  │
│  │ │                           │ │  │
│  │ │ Customer is at HIGH risk  │ │  │
│  │ │ of churning.              │ │  │
│  │ └───────────────────────────┘ │  │
│  └───────────────────────────────┘  │
└─────────────────────────────────────┘
```

### Layout Grid

**Sidebar Container:**
- Width: Streamlit default (280px typical)
- Padding: Streamlit native sidebar padding
- Background: Inherits from Streamlit theme (overridden by Bosk8 CSS)

**Form Section:**
- Title: "SINGLE-CUSTOMER SCORING" (label class, uppercase)
- Field spacing: `var(--space-1)` between inputs
- Group spacing: `var(--space-1_5)` between logical groups

**Result Card:**
- Padding: `var(--space-1)`
- Background: `var(--surface-card)`
- Border: `var(--border-w)` solid `var(--border-color)`
- Border-radius: `var(--r-md)`

### Components

1. **Form Title**
   - Text: "SINGLE-CUSTOMER SCORING"
   - Class: `label` (uppercase, letter-spacing 0.05em, text-muted)
   - Font-size: Inherits from base (0.875rem typical)

2. **Numeric Inputs (3)**
   - Labels: "Tenure", "MonthlyCharges", "TotalCharges"
   - Type: `st.number_input()` (Streamlit native)
   - Min/Max: Context-appropriate ranges
   - Step: 1 for Tenure, 0.01 for charges
   - Style: Inherit Bosk8 via CSS injection

3. **Categorical Selects (16)**
   - Labels: Feature names (uppercase via CSS)
   - Type: `st.selectbox()` (Streamlit native)
   - Options: Derived from training data (hardcoded or from model pipeline)
   - Style: Inherit Bosk8 via CSS injection

4. **Submit Button**
   - Text: "SCORE CUSTOMER"
   - Type: `st.button()` (Streamlit native)
   - Style: Minimal (Bosk8 doesn't specify button, derive from link style)

5. **Result Card**
   - Probability: Large number, formatted "XX.X%"
   - Risk Badge: Text-based, color-coded
   - Actionable text: Sentence explaining risk level

### Feature Field Specifications

**Numeric Features:**
- `tenure`: Integer, 0-72 months, step=1
- `MonthlyCharges`: Float, 0-200, step=0.01
- `TotalCharges`: Float, 0-10000, step=0.01

**Categorical Features (16):**
1. `gender`: ["Male", "Female"]
2. `SeniorCitizen`: ["No", "Yes"]
3. `Partner`: ["No", "Yes"]
4. `Dependents`: ["No", "Yes"]
5. `PhoneService`: ["No", "Yes"]
6. `MultipleLines`: ["No", "Yes", "No phone service"]
7. `InternetService`: ["DSL", "Fiber optic", "No"]
8. `OnlineSecurity`: ["No", "Yes", "No internet service"]
9. `OnlineBackup`: ["No", "Yes", "No internet service"]
10. `DeviceProtection`: ["No", "Yes", "No internet service"]
11. `TechSupport`: ["No", "Yes", "No internet service"]
12. `StreamingTV`: ["No", "Yes", "No internet service"]
13. `StreamingMovies`: ["No", "Yes", "No internet service"]
14. `Contract`: ["Month-to-month", "One year", "Two year"]
15. `PaperlessBilling`: ["No", "Yes"]
16. `PaymentMethod`: ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"]

Rating: Corrected typo: "OnlineBackup和处理" → "OnlineBackup"

### Responsive Rules

**Mobile (< 768px):**
- Sidebar: Hidden by default (Streamlit hamburger menu)
- Form: Full-width when opened
- Inputs: Stack vertically, full width

**Desktop (≥ 768px):**
- Sidebar: Always visible (collapsible)
- Form: Fixed width (Streamlit default)

### States

**Default State:**
- All inputs empty (or default values if set)
- Submit button enabled
- Result card hidden

**Filled State:**
- Inputs contain user-selected values
- Submit button enabled

**Submitting State:**
- Submit button shows loading indicator (Streamlit native)
- Result card hidden (or previous result visible)

**Result State:**
- Probability displayed: "XX.X%"
- Risk badge visible: [LOW RISK] / [MEDIUM RISK] / [HIGH RISK]
- Actionable text: "Customer is at [LEVEL] risk of churning."
- Submit button enabled (ready for new submission)

**Error State (Model Missing):**
- Form inputs disabled (grayed out)
- Error message: "Model artifact not found. Run training script first."
- Submit button hidden or disabled

**Error State (Validation):**
- Streamlit native validation (required field missing)
- Inline error message below problematic input
- Submit prevented until validation passes

**Error State (Prediction Failure):**
- Result card shows error message
- Text: "Prediction failed. Please check inputs and try again."
- Technical details optional (for debugging)

### Interaction Details

**Input Validation:**
- Client-side (Streamlit native)
- Required fields enforced
- Numeric range validation (min/max)
- Real-time feedback on invalid input

**Submit Behavior:**
- Triggers feature vector construction
- Runs model.predict_proba()
- Displays result immediately below form
- Clears previous result on new submission

**Result Display:**
- Probability rounded to 1 decimal place
- Risk thresholds:
  - Low: 0.0 - 0.4 (green accent, text-success)
  - Medium: 0.4 - 0.7 (text-muted)
  - High: 0.7 - 1.0 (text-primary, bold)

## Screen States Summary

### All Screens: Loading
- Streamlit spinner during initial load
- Artifact loading (model.joblib, top_risk.csv, metrics.json)
- Estimated time: < 2 seconds

### All Screens: Error (Artifacts Missing)
- Graceful degradation
- Error cards with actionable messages
- No crashes, informative feedback

### All Screens: Empty
- First-time deployment state
- All error cards visible
- Clear guidance to run training/scoring scripts

### All Screens: Success
- All artifacts loaded
- Data displayed correctly
- Form functional
- Metrics visible

