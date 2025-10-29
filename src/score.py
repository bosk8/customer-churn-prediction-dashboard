import pandas as pd
import joblib

# Load model and data
model = joblib.load("artifacts/model.joblib")
df = pd.read_csv("data/raw/telco_churn.csv")

# Generate predictions
scores = model.predict_proba(df.drop(columns=["Churn", "customerID"]))[:, 1]

# Create output with customer IDs and scores
out = df.assign(churn_score=scores).sort_values("churn_score", ascending=False)

# Export top 500 at-risk customers
out[["customerID", "churn_score"]].head(500).to_csv("artifacts/top_risk.csv", index=False)

print(f"Top 500 at-risk customers saved to artifacts/top_risk.csv")

