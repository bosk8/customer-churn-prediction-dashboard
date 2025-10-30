# Executive Summary

## Project Goals

**Primary Objective:** Deliver a production-ready customer churn prediction dashboard that enables business users to identify and act on at-risk customers through an intuitive, visually consistent interface adhering to the Bosk8 design system.

**Success Metrics:**
- ROC AUC ≥ 0.75 model performance (backend requirement)
- Top 500 at-risk customers surfaced in interactive table
- Single-customer scoring capability for ad-hoc predictions
- Zero-context deployment on Streamlit Community Cloud
- Full adherence to Bosk8 style guide (style.md)

## Primary Personas

### 1. Business Analyst / Data Analyst
- **Goals:** Quickly identify high-risk customers for retention campaigns
- **Needs:** Sortable risk list, export capability, model confidence metrics
- **Technical Level:** Intermediate (comfortable with data tables, understands probabilities)
- **Frequency:** Daily/weekly review sessions

### 2. Customer Success Manager
- **Goals:** Score individual customers to prioritize outreach
- **Needs:** Simple form input, clear probability display, actionable thresholds
- **Technical Level:** Low-intermediate (uses CRM tools, less ML-savvy)
- **Frequency:** Ad-hoc, as-needed queries

### 3. Data Scientist / ML Engineer
- **Goals:** Monitor model performance, validate predictions, retrain as needed
- **Needs:** Model metrics display, artifact versioning visibility, technical details
- **Technical Level:** High (understands ROC AUC, preprocessing pipelines)
- **Frequency:** Weekly model reviews, post-retraining verification

## Major User Flows

### Flow 1: Review Top At-Risk Customers (Primary Flow)
1. User opens dashboard → lands on main risk table view
2. System loads `artifacts/top_risk.csv` (pre-computed top 500)
3. User sees sortable table: `customerID`, `churn_score` columns
4. User can:
   - Sort by score (default: descending)
   - View model performance metric (ROC AUC) in header
   - Export table (via Streamlit native download)
5. User identifies customers to contact → exports list → closes dashboard

**Estimated time:** 2-5 minutes

### Flow 2: Single-Customer Scoring (Secondary Flow)
1. User opens dashboard → navigates to sidebar form
2. User inputs customer features:
   - Demographics: Gender, SeniorCitizen, Partner, Dependents
   - Services: PhoneService, MultipleLines, InternetService, OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport, StreamingTV, StreamingMovies
   - Account: Contract, PaperlessBilling, PaymentMethod
   - Usage: Tenure (months), MonthlyCharges, TotalCharges
3. User clicks "Score Customer" button
4. System:
   - Validates inputs (required fields, numeric ranges)
   - Constructs feature vector matching training schema
   - Runs model.predict_proba()
   - Displays churn probability with visual indicator
5. User reviews result → optionally adjusts inputs → rescore

**Estimated time:** 3-7 minutes per customer

### Flow 3: Model Performance Check (Tertiary Flow)
1. User secretly wants to verify model quality
2. User opens dashboard → sees ROC AUC in header card
3. User confirms AUC ≥ 0.75 threshold → continues with confidence
4. If AUC missing/low → user knows to retrain model

**Estimated time:** 5 seconds (passive verification)

## Constraints

### Technical Constraints
- **Platform:** Streamlit (single-page app, no native routing)
- **Styling:** Must inject CSS via `st.markdown(unsafe_allow_html=True)` — limited customization of native Streamlit components
- **Data:** Pre-computed CSV (`artifacts/top_risk.csv`) — no live database connection
- **Model:** Pre-loaded joblib artifact — no API endpoints, must exist on filesystem
- **Deployment:** Streamlit Community Cloud — public repo, 1GB limit, no custom domains

### Design Constraints
- **Style System:** Bosk8 Dark Minimal Mono (style.md) — all tokens must reference exact names
- **Responsive:** Mobile-first, breakpoints: 768px (tablet), 1024px (desktop)
- **Accessibility:** WCAG 2.2 AA minimum — contrast ratios, keyboard navigation, ARIA labels
- **Performance:** Dashboard must load in <3s on Community Cloud (artifact file sizes matter)

### Functional Constraints
- **Single Page:** No multi-page navigation (Streamlit limitation)
- **No Authentication:** Public dashboard (assumes artifact security handled at repo level)
- **No Real-time Updates:** Batch-scored data, refreshed via re-running `score.py`
- **Limited Validation:** Client-side only (Streamlit form validation + Python assertions)

## Assumptions & Open Questions

### Recorded Assumptions
1. **Data Schema:** Telco dataset includes standard columns (gender, tenure, MonthlyCharges, TotalCharges, etc.) — if columns differ, form will need adjustment
2. **Feature Count:** ~19 features (3 numeric, 16 categorical) — form UI scales to accommodate all
3. **Missing Values:** TotalCharges may have empty strings converted to NaN — handled in preprocessing
4. **Model Output:** Binary classification probability [0, 1] displayed as percentage
5. **Table Size:** Top 500 rows manageable for Streamlit dataframe component (native pagination)
6. **Browser Support:** Modern browsers (Chrome, Firefox, Safari, Edge) — CSS variables supported

### Open Questions (Resolved by Inference)
1. **Form Layout:** Sidebar vs. inline? → **Resolved:** Sidebar (as per project-scope.md example)
2. **Export Format:** CSV vs. Excel? → **Resolved:** CSV (Streamlit native, aligns with artifacts)
3. **Probability Display:** Number only vs. visual gauge? → **Resolved:** Number + color-coded badge (using success accent for low risk inverse)
4. **Error Handling:** Toast notifications vs. inline messages? → **Resolved:** Inline error cards (matches Bosk8 minimal aesthetic)
5. **Loading States:** Spinner vs. skeleton? → **Resolved:** Minimal text indicator (Bosk8 utilitarian style)

### Style-Derived Decisions
1. **Colors:** Only grayscale + green success accent (no error red, use text-subtle for warnings)
2. **Typography:** All labels uppercase, JetBrains Mono, 0.05em letter-spacing
3. **Spacing:** Dense but breathable — use spacing tokens from style.md
4. **Borders:** Thin borders (1px mobile, 1.5px desktop) for structure, not decoration
5. **Radii:** Small (4px sm, 6px md) — no aggressive rounding

## Non-Goals

Explicitly out of scope:
- User authentication/authorization
- Real-time model retraining from dashboard
- Historical prediction tracking/analytics
- Customer detail drill-down pages
- Data export beyond CSV
- Custom visualizations (charts, graphs)
- Model interpretability features (SHAP, feature importance)
- Multi-model comparison views
- A/B testing framework
- Mobile app (web-only)

