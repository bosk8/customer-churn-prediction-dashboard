import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Churn Predictor", layout="wide")
st.title("Customer Churn Prediction")

# Load model (required for single-customer scoring)
try:
    model = joblib.load("artifacts/model.joblib")
    model_loaded = True
except FileNotFoundError:
    st.error("Model artifact not found. Please run training script first.")
    model_loaded = False

st.header("Top 500 at-risk customers")

# Load and display top risk customers
try:
    df = pd.read_csv("artifacts/top_risk.csv")
    st.dataframe(df, use_container_width=True)
except FileNotFoundError:
    st.error("Top risk CSV not found. Please run scoring script first.")

# Optional single-customer form in sidebar
st.sidebar.header("Single-customer form (optional)")
st.sidebar.caption("Build inputs to score a hypothetical customer.")
st.sidebar.info("Feature input form would go here. This is a placeholder implementation.")

