import streamlit as st
import pandas as pd
import joblib
import json
import numpy as np

st.set_page_config(page_title="Churn Predictor", layout="wide")

# Inject Bosk8 CSS variables and base styles from style.md
st.markdown(
    """
<style>
:root {
  --font-ui: JetBrains Mono, ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, DejaVu Sans Mono, Courier New, monospace;
  --fs-base: clamp(16px, calc(15.2px + 0.25vw), 20px);
  --bg-black: #000;
  --bg-elev1: #0A0A0A;
  --surface-card: #09090B;
  --text-primary: #fff;
  --text-muted: #e8e8e8;
  --text-subtle: #a1a1aa;
  --text-dim: #71717a;
  --text-highlight: #f4f4f5;
  --accent-success: #22c55e;
  --border-color: rgb(39 39 42);
  --border-w: 1px;
  --border-outer-w: 1px;
  --shadow-tint: #0000000d;
  --r-sm: 4px;
  --r-md: 6px;
}
@media (min-width: 1024px) {
  :root { --border-w: 1.5px; --border-outer-w: 2px; }
}
* { box-sizing: border-box; margin: 0; padding: 0; }
html { font-size: var(--fs-base); }
html, body { background-color: var(--bg-black); font-family: var(--font-ui); color: var(--text-primary); }
main.bosk8 { display:flex; flex-direction:column; align-items:center; justify-content:center; min-height: 100vh; padding: 4rem 1rem 1rem; padding-top: 10rem; background-color: var(--bg-elev1); }
.container { width: 100%; max-width: min(1100px, 90vw); position: relative; }
.card { background-color: var(--surface-card); box-shadow: 0 0 0 var(--border-outer-w) var(--border-color), 0 1px 2px var(--shadow-tint); border-radius: var(--r-md); }
.border-b { border-bottom: var(--border-w) solid var(--border-color); }
.tagline, .meta, .label, .nav { text-transform: uppercase; letter-spacing: 0.05em; color: var(--text-muted); }
.tagline { font-size: 1rem; text-align: center; }
.meta-sm { font-size: 0.75rem; }
.meta-md { font-size: 0.875rem; }
.link { color: var(--text-muted); text-decoration: none; transition: all .15s; }
.link:hover { color: var(--text-primary); text-decoration: underline; text-underline-offset: 4px; }
:focus-visible { outline: 2px solid var(--border-color); outline-offset: 2px; }
.table-card { padding: 1rem; }
.metrics-card { padding: 2rem; display:flex; flex-direction:column; gap: .5rem; align-items:center; }
.error-card { padding: 1rem; color: var(--text-subtle); }
</style>
""",
    unsafe_allow_html=True,
)

# Load model (required for single-customer scoring)
try:
    model = joblib.load("artifacts/model.joblib")
    model_loaded = True
except FileNotFoundError:
    st.markdown("""
<div class="card error-card">
  <div class="meta-sm">Model artifact not found. Run training script first.</div>
</div>
""", unsafe_allow_html=True)
    model_loaded = False

# Metrics card (AUC)
auc_value = None
try:
    with open("artifacts/metrics.json", "r") as f:
        m = json.load(f)
        auc_value = float(m.get("roc_auc"))
except Exception:
    pass

st.markdown("""
<main class="bosk8">
  <div class="container">
    <section class="card metrics-card border-b">
      <h1 class="tagline">CUSTOMER CHURN DASHBOARD</h1>
      <p class="meta-sm">{auc}</p>
    </section>
  </div>
</main>
""".format(auc=(f"ROC AUC: {auc_value:.3f}" if auc_value is not None else "AUC unavailable")), unsafe_allow_html=True)

# Load and display top risk customers inside a card
try:
    df = pd.read_csv("artifacts/top_risk.csv")
    st.markdown('<div class="card table-card border-b"><div class="meta-md">Top 500 at-risk customers</div>', unsafe_allow_html=True)
    st.dataframe(df, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
except FileNotFoundError:
    st.markdown("""
<div class="card error-card">
  <div class="meta-sm">Top risk CSV not found. Run scoring script first.</div>
</div>
""", unsafe_allow_html=True)

# Single-customer scoring form in sidebar
st.sidebar.markdown("<div class='label' style='margin-bottom: 1rem;'>SINGLE-CUSTOMER SCORING</div>", unsafe_allow_html=True)
st.sidebar.caption("Enter customer features to predict churn probability.")

if model_loaded:
    with st.sidebar.form("customer_scoring_form"):
        # Demographics Section
        st.markdown("<div style='color: var(--text-muted); font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.05em; margin-top: 1.5rem; margin-bottom: 0.5rem;'>DEMOGRAPHICS</div>", unsafe_allow_html=True)
        
        gender = st.selectbox("Gender", ["Male", "Female"], key="gender")
        senior_citizen = st.selectbox("Senior Citizen", ["No", "Yes"], key="senior_citizen")
        partner = st.selectbox("Partner", ["No", "Yes"], key="partner")
        dependents = st.selectbox("Dependents", ["No", "Yes"], key="dependents")
        
        # Services Section
        st.markdown("<div style='color: var(--text-muted); font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.05em; margin-top: 1.5rem; margin-bottom: 0.5rem;'>SERVICES</div>", unsafe_allow_html=True)
        
        phone_service = st.selectbox("Phone Service", ["No", "Yes"], key="phone_service")
        multiple_lines = st.selectbox("Multiple Lines", ["No", "Yes", "No phone service"], key="multiple_lines")
        internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"], key="internet_service")
        online_security = st.selectbox("Online Security", ["No", "Yes", "No internet service"], key="online_security")
        online_backup = st.selectbox("Online Backup", ["No", "Yes", "No internet service"], key="online_backup")
        device_protection = st.selectbox("Device Protection", ["No", "Yes", "No internet service"], key="device_protection")
        tech_support = st.selectbox("Tech Support", ["No", "Yes", "No internet service"], key="tech_support")
        streaming_tv = st.selectbox("Streaming TV", ["No", "Yes", "No internet service"], key="streaming_tv")
        streaming_movies = st.selectbox("Streaming Movies", ["No", "Yes", "No internet service"], key="streaming_movies")
        
        # Account Section
        st.markdown("<div style='color: var(--text-muted); font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.05em; margin-top: 1.5rem; margin-bottom: 0.5rem;'>ACCOUNT</div>", unsafe_allow_html=True)
        
        contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"], key="contract")
        paperless_billing = st.selectbox("Paperless Billing", ["No", "Yes"], key="paperless_billing")
        payment_method = st.selectbox("Payment Method", [
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)"
        ], key="payment_method")
        
        # Usage Section
        st.markdown("<div style='color: var(--text-muted); font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.05em; margin-top: 1.5rem; margin-bottom: 0.5rem;'>USAGE</div>", unsafe_allow_html=True)
        
        tenure = st.number_input("Tenure (months)", min_value=0, max_value=72, value=0, step=1, key="tenure")
        monthly_charges = st.number_input("Monthly Charges", min_value=0.0, max_value=200.0, value=0.0, step=0.01, format="%.2f", key="monthly_charges")
        total_charges = st.number_input("Total Charges", min_value=0.0, max_value=10000.0, value=0.0, step=0.01, format="%.2f", key="total_charges")
        
        # Submit Button
        submitted = st.form_submit_button("SCORE CUSTOMER", use_container_width=True)
        
        # Process form submission
        if submitted:
            try:
                # Construct feature DataFrame matching training schema
                
                # Create DataFrame with all features in correct order
                # Match the exact column names and data types from training
                feature_dict = {
                    "gender": gender,
                    "SeniorCitizen": 1 if senior_citizen == "Yes" else 0,  # Numeric: 0 or 1
                    "Partner": partner,
                    "Dependents": dependents,
                    "tenure": float(tenure),
                    "PhoneService": phone_service,
                    "MultipleLines": multiple_lines,
                    "InternetService": internet_service,
                    "OnlineSecurity": online_security,
                    "OnlineBackup": online_backup,
                    "DeviceProtection": device_protection,
                    "TechSupport": tech_support,
                    "StreamingTV": streaming_tv,
                    "StreamingMovies": streaming_movies,
                    "Contract": contract,
                    "PaperlessBilling": paperless_billing,
                    "PaymentMethod": payment_method,
                    "MonthlyCharges": float(monthly_charges),
                    "TotalCharges": float(total_charges)
                }
                
                # Create DataFrame (single row)
                feature_df = pd.DataFrame([feature_dict])
                
                # Ensure numeric columns are numeric (matches training select_dtypes logic)
                # The model pipeline will handle preprocessing (StandardScaler for numeric, OneHotEncoder for categorical)
                
                # Use model to predict probability
                probability = model.predict_proba(feature_df)[0, 1]
                
                # Determine risk level
                if probability < 0.4:
                    risk_level = "LOW"
                    risk_color = "var(--accent-success)"
                    risk_text = "LOW"
                elif probability < 0.7:
                    risk_level = "MEDIUM"
                    risk_color = "var(--text-muted)"
                    risk_text = "MEDIUM"
                else:
                    risk_level = "HIGH"
                    risk_color = "var(--text-primary)"
                    risk_text = "HIGH"
                
                # Display result card
                st.markdown(f"""
                <div class="card" style="padding: var(--space-1); border: var(--border-w) solid var(--border-color); border-radius: var(--r-md); margin-top: 1rem;">
                  <div style="font-size: 1.5rem; color: var(--text-primary); font-family: var(--font-ui); margin-bottom: 0.5rem;">{probability:.1%}</div>
                  <div style="color: {risk_color}; font-weight: bold; text-transform: uppercase; letter-spacing: 0.05em; font-family: var(--font-ui); margin-bottom: 0.5rem;">{risk_text} RISK</div>
                  <div style="color: var(--text-muted); font-family: var(--font-ui); font-size: 0.875rem;">Customer is at {risk_level} risk of churning.</div>
                </div>
                """, unsafe_allow_html=True)
                
            except Exception as e:
                st.markdown(f"""
                <div class="card error-card" style="margin-top: 1rem;">
                  <div class="meta-sm">Prediction failed. Please check inputs and try again.</div>
                  <div class="meta-sm" style="margin-top: 0.5rem; color: var(--text-dim);">Error: {str(e)}</div>
                </div>
                """, unsafe_allow_html=True)
else:
    st.sidebar.markdown("""
    <div class="card error-card">
      <div class="meta-sm">Model artifact not found. Run training script first.</div>
    </div>
    """, unsafe_allow_html=True)

