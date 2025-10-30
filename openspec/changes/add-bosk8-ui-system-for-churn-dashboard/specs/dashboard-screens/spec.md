## ADDED Requirements

### Requirement: Dashboard Layout
The dashboard SHALL render a single-page layout with `main.bosk8` containing a `.container` and three sections: metrics card, risk table card, and optional sidebar form.

#### Scenario: Metrics card
- **WHEN** `artifacts/metrics.json` exists
- **THEN** display ROC AUC value in a `.card` with `.tagline` and `.meta-sm`

#### Scenario: Risk table
- **WHEN** `artifacts/top_risk.csv` exists
- **THEN** display a sortable table within a `.card` using `--surface-card` and `--border-w`

#### Scenario: Empty states
- **WHEN** artifacts are missing
- **THEN** show error content in a `.card` using `--text-subtle` guidance and recovery steps

### Requirement: Detail Drawer/Modal
The system MUST provide a detail view of a selected customer in a `.card` surface.

#### Scenario: Open detail
- **WHEN** a table row is activated
- **THEN** show key attributes and `churn_score` with `.meta-md` labels

### Requirement: Sidebar Scoring Form
The system MUST provide an optional single-customer scoring form in the sidebar with labeled inputs and submit.

#### Scenario: Loading and error states
- **WHEN** scoring is in progress
- **THEN** show loading feedback within ≤200ms transitions
- **WHEN** validation fails
- **THEN** show inline error styling using `--text-subtle` and border `--border-color`

## MODIFIED Requirements

## REMOVED Requirements


