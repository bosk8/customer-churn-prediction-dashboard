## Context

This is a greenfield project to build a customer churn prediction system from scratch. The system must be end-to-end, reproducible, and deployable to Streamlit Community Cloud. The primary goal is to identify the top 500 at-risk customers based on predicted churn probability.

## Goals / Non-Goals

### Goals
- Train ML models (logistic regression and random forest) on IBM Telco Customer Churn dataset
- Achieve ROC AUC ≥ 0.75 on test set
- Generate batch predictions and export top 500 at-risk customers
- Create interactive Streamlit dashboard for visualization
- Deploy to Streamlit Community Cloud as public application
- Maintain reproducibility through saved artifacts and clear documentation

### Non-Goals
- Deep learning models (tabular ML with scikit-learn only)
- Time-series survival analysis
- Real-time streaming predictions
- PII data ingestion or privacy-preserving techniques beyond dropping customerID
- Model serving API (dashboard-only interface)
- Advanced feature engineering beyond basic preprocessing

## Decisions

### Decision: Use scikit-learn Pipeline for preprocessing and modeling
**Rationale**: Ensures consistent preprocessing between training and scoring, prevents data leakage, and simplifies model persistence.
**Alternatives considered**: 
- Manual preprocessing → Rejected due to risk of inconsistency
- Using separate transformers → Rejected as Pipeline provides better encapsulation

### Decision: Evaluate two model candidates (LogisticRegression and RandomForestClassifier)
**Rationale**: Provides model comparison, RandomForest captures non-linear relationships while LogisticRegression offers interpretability baseline. Both are standard tabular ML approaches.
**Alternatives considered**:
- Single model approach → Rejected; comparison provides better performance assurance
- More complex ensemble → Rejected; violates "minimal features" scope requirement

### Decision: Save model suboptimal AUC triggers retraining/tuning
**Rationale**: Success criteria explicitly require AUC ≥ 0.75; failing models should be improved before deployment.
**Alternatives considered**:
- Deploy regardless → Rejected; violates success criteria
- Manual threshold adjustment → Considered but threshold tuning is separate from AUC metric

### Decision: Batch scoring generates static CSV file
**Rationale**: Simpler than database integration, sufficient for dashboard display, aligns with "minimal features" scope.
**Alternatives considered**:
- Real-time scoring via API → Rejected; out of scope (dashboard-only)
- Database storage → Rejected; adds complexity without clear requirement

### Decision: Streamlit dashboard displays pre-computed top 500 list
**Rationale**: Meets requirements efficiently, avoids unnecessary real-time computation, faster dashboard load times.
**Alternatives considered**:
- Dynamic real-time sorting → Considered but unnecessary given batch scoring approach

## Risks / Trade-offs

### Risk: Model fails to achieve AUC ≥ 0.75
**Mitigation**: Include hyperparameter tuning step in training script, consider feature interactions if initial models fail, document troubleshooting steps.

### Risk: Categorical encoding issues with unseen categories
**Mitigation**: Use `OneHotEncoder(handle_unknown="ignore")` to gracefully handle unknown categories during scoring.

### Risk: Class imbalance affecting model performance
**Mitigation**: Use `class_weight="balanced"` for LogisticRegression, RandomForest handles imbalance natively.

### Risk: Missing values in dataset
**Mitigation**: EDA phase will identify and document missing value strategy; scikit-learn transformers handle NaN appropriately for numeric features.

### Trade-off: Static batch scoring vs real-time predictions
**Acceptance**: Batch scoring is sufficient for daily/weekly risk list updates and simpler to implement. Real-time can be added later if needed.

## Migration Plan

N/A - This is a greenfield implementation with no existing system to migrate from.

## Open Questions

None identified at this time. The project scope is well-defined and implementation path is clear.
