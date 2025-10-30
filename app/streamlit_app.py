import streamlit as st
import pandas as pd
import joblib
import json

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

# Optional single-customer form in sidebar (styled labels)
st.sidebar.markdown("<div class='label'>Single-customer form (optional)</div>", unsafe_allow_html=True)
st.sidebar.caption("Build inputs to score a hypothetical customer.")
st.sidebar.info("Feature input form would go here. This is a placeholder implementation.")

