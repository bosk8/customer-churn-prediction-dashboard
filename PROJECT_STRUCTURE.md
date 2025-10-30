# Project Structure

## Directory Layout

```
02-customer-churn-prediction-dashboard/
├── app/                          # Streamlit application
│   └── streamlit_app.py         # Main dashboard application
│
├── artifacts/                   # Generated model artifacts (gitignored)
│   ├── model.joblib            # Trained model (generated)
│   ├── metrics.json            # Model metrics (generated)
│   └── top_risk.csv            # Top 500 at-risk customers (generated)
│
├── data/                        # Data files
│   └── raw/                    # Raw data files
│       └── telco_churn.csv     # IBM Telco Customer Churn dataset
│
├── docs/                        # Project documentation
│   ├── README.md               # Documentation index
│   ├── IMPLEMENTATION_STATUS.md # Implementation status report
│   ├── SANITY_CHECK_REPORT.md  # Sanity check verification
│   └── project-scope.md        # Project scope and requirements
│
├── env/                        # Environment configuration
│   └── requirements.txt        # Python dependencies
│
├── notebooks/                  # Jupyter notebooks
│   └── 01_eda.ipynb           # Exploratory data analysis
│
├── specs/                      # UI/UX specification documents
│   ├── README.md              # Specifications index
│   ├── executive-summary.md   # Project goals, personas, flows
│   ├── information-architecture.md # Sitemap and user flows
│   ├── screens.md              # Screen-by-screen specifications
│   ├── components.md          # Interactive component library
│   ├── function-to-ui-mapping.md # Backend to UI mapping
│   ├── accessibility-checklist.md # WCAG 2.2 AA compliance
│   ├── style-compliance-matrix.md # Style token mappings
│   ├── style-decisions-log.md  # Assumptions and derivations
│   └── dev-handoff.md         # Developer handoff artifacts
│
├── src/                        # Source code
│   ├── train.py               # Model training script
│   └── score.py               # Batch scoring script
│
├── README.md                   # Project overview and usage
└── PROJECT_STRUCTURE.md        # This file
```

## Folder Descriptions

### `app/`
Streamlit dashboard application. Contains the main `streamlit_app.py` file that implements the UI according to Bosk8 design system specifications.

### `artifacts/`
Generated model artifacts (not committed to git). Created by running `src/train.py` and `src/score.py`:
- `model.joblib` - Trained scikit-learn model pipeline
- `metrics.json` - Model performance metrics (ROC AUC)
- `top_risk.csv` - Top 500 at-risk customers with churn scores

### `data/`
Data files for the project. Contains the raw Telco Customer Churn dataset.

### `docs/`
Project documentation including:
- Implementation status reports
- Sanity check reports
- Project scope and requirements

### `env/`
Environment configuration files. Contains Python dependencies in `requirements.txt`.

### `notebooks/`
Jupyter notebooks for exploratory data analysis and prototyping.

### `specs/`
Complete UI/UX specification documentation system:
- Executive summary and project goals
- Information architecture and user flows
- Screen-by-screen specifications with wireframes
- Interactive component library
- Function-to-UI mapping
- Accessibility checklist
- Style compliance matrix
- Style decisions log
- Developer handoff artifacts

### `src/`
Source code scripts:
- `train.py` - Model training pipeline
- `score.py` - Batch scoring script

## Key Files

### Root Level
- **README.md** - Main project documentation with installation, usage, and deployment instructions
- **PROJECT_STRUCTURE.md** - This file (directory structure documentation)

### Documentation
- **docs/project-scope.md** - Project scope, requirements, and build steps
- **docs/IMPLEMENTATION_STATUS.md** - Complete implementation status report
- **docs/SANITY_CHECK_REPORT.md** - Comprehensive sanity check verification

### Specifications
- **specs/README.md** - Specification documentation index
- **specs/dev-handoff.md** - Developer handoff with CSS tokens, snippets, acceptance checklist

## Workflow

1. **Data Preparation**: Place `telco_churn.csv` in `data/raw/`
2. **Model Training**: Run `python src/train.py` → generates `artifacts/model.joblib` and `artifacts/metrics.json`
3. **Batch Scoring**: Run `python src/score.py` → generates `artifacts/top_risk.csv`
4. **Dashboard**: Run `streamlit run app/streamlit_app.py` → launches interactive dashboard

## Notes

- All artifacts are generated files (not committed to git)
- Specification documents in `specs/` are complete and production-ready
- Documentation in `docs/` provides status and verification reports
- Source code in `src/` implements the ML pipeline
- Application code in `app/` implements the Streamlit dashboard

