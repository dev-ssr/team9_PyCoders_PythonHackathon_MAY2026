import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

st.set_page_config(page_title="HUPA-UCM Diabetes Dashboard", layout="wide")

st.title("HUPA-UCM Diabetes Analytics Dashboard")

# Create tabs
tab1, tab2, tab3 = st.tabs([
    "Descriptive Analysis",
    "Prescriptive Analysis",
    "Predictive Analysis"
])import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Set page config
st.set_page_config(page_title="Diabetes Analysis Dashboard", layout="wide")

# --- CUSTOM CSS ---
st.markdown("""
<style>
.stApp { background-color: #FFFFFF; }
h1 { font-size: 70px !important; color: #0B243B !important; text-align: center; font-weight: 800 !important; }
</style>
""", unsafe_allow_html=True)

# =========================
# FIXED DATA LOADER
# =========================
@st.cache_data
def load_data():
    try:
        df = pd.read_csv("Team9_Pycoders_clean.csv")
    except FileNotFoundError:
        st.error("❌ Team9_Pycoders_clean.csv not found in project folder")
        st.stop()

    df['time'] = pd.to_datetime(df['time'])
    df['hour'] = df['time'].dt.hour
    return df

df = load_data()

# =========================
# KPI CALCULATION
# =========================
def glucose_category(glucose):
    if glucose < 140:
        return "Normal"
    elif glucose < 180:
        return "Prediabetic"
    else:
        return "Diabetic"

df["Glucose_Category"] = df["glucose"].apply(glucose_category)

total_patients = df["Patient_ID"].nunique()
avg_glucose = round(df["glucose"].mean(), 2)
avg_heart_rate = round(df["heart_rate"].mean(), 2)
avg_steps = round(df["steps"].mean(), 2)

normal_glucose_percent = round(
    (df[df["Glucose_Category"] == "Normal"].shape[0] / len(df)) * 100, 2
)

# =========================
# HEADER
# =========================
st.markdown("<h1>Diabetes Analysis Dashboard</h1>", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Patients", total_patients)
with col2:
    st.metric("Avg Glucose", avg_glucose)
with col3:
    st.metric("Heart Rate", avg_heart_rate)
with col4:
    st.metric("Normal %", f"{normal_glucose_percent}%")

st.markdown("---")

# =========================
# SIMPLE CHART (SAFE)
# =========================
st.subheader("Glucose Distribution")

fig = px.histogram(df, x="glucose", nbins=30, color_discrete_sequence=["#2E86C1"])
st.plotly_chart(fig, use_container_width=True)

# =========================
# NOTE
# =========================
st.info("✔ App is running successfully with Team9_Pycoders_clean.csv")

# =====================================================
# DESCRIPTIVE ANALYSIS TAB
# =====================================================

with tab1:
    st.header("Descriptive Analysis")

    st.markdown("""
    This section explores glucose trends, insulin usage, activity patterns,
    heart rate, calories, and patient-level behavior.
    """)

    st.info("Add your descriptive charts here.")


# =====================================================
# PREDICTIVE ANALYSIS TAB
# =====================================================

with tab3:
    st.header("Predictive Analysis")

    st.markdown("""
    This section compares machine learning and deep learning models
    for forecasting future glucose values.
    """)

    results = pd.DataFrame({
        "Model": [
            "Linear Regression",
            "XGBoost",
            "LSTM",
            "GRU"
        ],
        "MAE": [
            29.22,
            25.05,
            0.99,
            10.77
        ],
        "RMSE": [
            43.81,
            39.82,
            1.81,
            15.52
        ],
        "R² Score": [
            0.418,
            0.512,
            0.998,
            0.859
        ]
    })

    st.subheader("Model Performance Metrics")
    st.dataframe(results, use_container_width=True)

    st.subheader("Performance Comparison")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("#### MAE")
        fig, ax = plt.subplots(figsize=(3, 2.5))
        ax.bar(results["Model"], results["MAE"])
        ax.set_ylabel("MAE", fontsize=8)
        ax.tick_params(axis="x", rotation=45, labelsize=7)
        ax.tick_params(axis="y", labelsize=7)
        st.pyplot(fig)

    with col2:
        st.markdown("#### RMSE")
        fig, ax = plt.subplots(figsize=(3, 2.5))
        ax.bar(results["Model"], results["RMSE"])
        ax.set_ylabel("RMSE", fontsize=8)
        ax.tick_params(axis="x", rotation=45, labelsize=7)
        ax.tick_params(axis="y", labelsize=7)
        st.pyplot(fig)

    with col3:
        st.markdown("#### R² Score")
        fig, ax = plt.subplots(figsize=(3, 2.5))
        ax.bar(results["Model"], results["R² Score"])
        ax.set_ylabel("R²", fontsize=8)
        ax.tick_params(axis="x", rotation=45, labelsize=7)
        ax.tick_params(axis="y", labelsize=7)
        st.pyplot(fig)

    st.subheader("Actual vs Predicted Glucose")

    linear_img = Image.open("charts/linear_regression.png")
    xgb_img = Image.open("charts/xgboost.png")
    lstm_img = Image.open("charts/lstm.png")
    gru_img = Image.open("charts/gru.png")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Linear Regression")
        st.image(linear_img, use_container_width=True)

    with col2:
        st.markdown("### XGBoost")
        st.image(xgb_img, use_container_width=True)

    col3, col4 = st.columns(2)

    with col3:
        st.markdown("### LSTM")
        st.image(lstm_img, use_container_width=True)

    with col4:
        st.markdown("### GRU")
        st.image(gru_img, use_container_width=True)

    st.subheader("Key Insights")

    st.markdown("""
    - **Linear Regression showed limited forecasting capability**, suggesting glucose behavior is nonlinear.
    - **XGBoost improved prediction accuracy** by capturing nonlinear relationships.
    - **LSTM achieved the best overall performance**, showing the strength of sequential deep learning.
    - **GRU also performed strongly**, capturing temporal glucose dynamics with lower complexity than LSTM.
    """)


# =====================================================
# PRESCRIPTIVE ANALYSIS TAB
# =====================================================

with tab2:
    st.header("Prescriptive Analysis")

    st.markdown("""
    This section provides recommendations based on glucose risk patterns,
    activity levels, insulin delivery, and lifestyle indicators.
    """)

    st.info("Add your prescriptive recommendations here.")