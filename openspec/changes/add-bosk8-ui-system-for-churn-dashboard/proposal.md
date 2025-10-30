## Why
The project needs a production-ready UI/UX system for the Streamlit-based churn dashboard that strictly adheres to the Bosk8 design language. This proposal introduces a reusable component library, screen specs, and accessibility patterns grounded in `style.md`.

## What Changes
- Define an application-wide UI system and component library bound to `style.md` tokens
- Specify information architecture, navigation, and user flows for the churn dashboard
- Provide screen-by-screen specs with exact tokens and interaction states
- Map backend training/scoring artifacts to UI surfaces and contracts
- Establish accessibility and compliance artifacts (WCAG 2.2 AA)
- Deliver developer handoff assets (CSS vars, redlines, snippets) using `style.md`

## Impact
- Affected specs: `ui-system`, `dashboard-screens`, `accessibility`, `routing`
- Affected code: `app/streamlit_app.py`, future UI modules/components; references to `artifacts/*.csv|*.joblib`

## Executive summary
Goals: enable analysts and managers to view the top 500 at-risk customers, inspect risk, and run single-customer what-if scoring, with consistent Bosk8 styling.
- Primary personas: Data Analyst (daily), Ops Manager (weekly)
- Major flows: view top risks, filter/sort, inspect record, re-run scoring, view metrics
- Constraints: Streamlit environment, local artifacts in `artifacts/`, single-page app preference

## Information Architecture
- Global: Single-page main route with sections
  - Hero/status card (metrics + model state)
  - Risk table (top 500)
  - Detail drawer/modal (customer details)
  - Sidebar: single-customer scoring form (optional)

## User Flows
Happy path:
1) Load app → model and top_risk CSV present → show metrics + table
2) User sorts/filters table → opens a customer → sees details
3) User adjusts form inputs → gets score → optional append preview row

Edge cases:
- Missing artifacts → show error card with recovery actions
- Long table load → show loading skeleton/spinner
- Form invalid → inline errors on required fields

## Screen-by-screen specs (overview)
- Dashboard: `main.bosk8` container, `card` sections, grid tiles for KPIs, data table with sticky header
- Detail drawer: card with meta text and key-value pairs
- Sidebar form: labeled inputs, submit, loading, error states

## Interactive Component Library (overview)
Components include Button, Card, Table, Tooltip, Accordion (FAQ), Tagline/Meta text, Form inputs. Variants and states bound to `style.md` tokens (see delta specs).

## Function-to-UI mapping
- Training (`src/train.py`) → Metrics card reads `artifacts/metrics.json`
- Scoring (`src/score.py`) → Risk table reads `artifacts/top_risk.csv`
- Model artifact (`artifacts/model.joblib`) → Enables sidebar scoring

## Navigation & routing
- Single route with anchored sections. Breadcrumb not required. Empty state messaging for first run.

## Accessibility checklist
- Color contrast using `--text-primary` on `--bg-elev1` and `--surface-card`
- Keyboard focus with `:focus-visible` outline `2px` `--border-color`
- Tooltips only on hover ≥768px; click-activated on mobile

## Style Compliance Matrix
Maintained in `style-compliance.md` with exact token references.

## Style Decisions Log
Maintained in `style-decisions-log.md` with assumptions and derivations per `style.md` rules.

## Dev handoff artifacts
Provided in `dev-handoff.md`: CSS var map, spacing/redlines, sample HTML/CSS snippets.


