import pandas as pd
import joblib

from src.config import MODEL_FILE, TOP_RISK_FILE
from src.data import load_data


def main():
    """
    Main function to run the scoring pipeline.
    """
    model = joblib.load(MODEL_FILE)
    df = load_data()

    X = df.drop(columns=["Churn", "customerID"])
    scores = model.predict_proba(X)[:, 1]

    out = df.assign(churn_score=scores).sort_values(
        "churn_score", ascending=False
    )

    out[["customerID", "churn_score"]].head(500).to_csv(
        TOP_RISK_FILE, index=False
    )

    print(f"Top 500 at-risk customers saved to {TOP_RISK_FILE}")


if __name__ == "__main__":
    main()
