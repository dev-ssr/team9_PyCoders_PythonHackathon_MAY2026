import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(page_title="Diabetes Analysis Dashboard", layout="wide")

# =========================
# CUSTOM CSS
# =========================
st.markdown("""
<style>
.stApp { background-color: #FFFFFF; }

h1 {
    font-size: 70px !important;
    color: #0B243B !important;
    text-align: center;
    font-weight: 800 !important;
}
</style>
""", unsafe_allow_html=True)

# =========================
# SAFE DATA LOADER (FIXED)
# =========================
@st.cache_data
def load_data():
    file_path = "Team9_Pycoders_clean.csv"   # ✅ FIXED FILE NAME

    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        st.error(f"❌ File not found: {file_path}. Please keep it in the same folder as app.py")
        st.stop()

    # Convert time safely
    if "time" in df.columns:
        df['time'] = pd.to_datetime(df['time'], errors='coerce')
        df['hour'] = df['time'].dt.hour

    return df

df = load_data()

# =========================
# BASIC CLEANING SAFETY
# =========================
required_cols = ["glucose", "heart_rate", "steps", "Patient_ID"]
missing_cols = [c for c in required_cols if c not in df.columns]

if missing_cols:
    st.error(f"❌ Missing columns in dataset: {missing_cols}")
    st.stop()

# =========================
# KPI CALCULATIONS
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
# SIMPLE CHART
# =========================
st.subheader("Glucose Distribution")

fig = px.histogram(
    df,
    x="glucose",
    nbins=30,
    color_discrete_sequence=["#2E86C1"]
)

st.plotly_chart(fig, use_container_width=True)

# =========================
# SUCCESS MESSAGE
# =========================
st.success("✅ Dashboard loaded successfully with Team9_Pycoders_clean.csv")