import streamlit as st
import pandas as pd
import plotly.express as px

# Page settings
st.set_page_config(page_title="HUPA Diabetes Dashboard", layout="wide")

st.title("HUPA Diabetes Data Dashboard")
st.write("Analysis of glucose trends, insulin, activity, sleep, and patient demographics.")

# Load data (IMPORTANT: clean.csv is one folder above Dashboard)
df = pd.read_csv("../clean.csv")

# Convert time column
df["time"] = pd.to_datetime(df["time"], errors="coerce")
df = df.dropna(subset=["time"])

# Sidebar filters
st.sidebar.header("Filters")

patients = st.sidebar.multiselect(
    "Select Patient ID",
    options=df["Patient_ID"].unique(),
    default=df["Patient_ID"].unique()
)

df_filtered = df[df["Patient_ID"].isin(patients)]

# KPI cards
col1, col2, col3, col4 = st.columns(4)

col1.metric("Average Glucose", round(df_filtered["glucose"].mean(), 2))
col2.metric("Average Heart Rate", round(df_filtered["heart_rate"].mean(), 2))
col3.metric("Average Steps", round(df_filtered["steps"].mean(), 2))
col4.metric("Average Sleep Duration", round(df_filtered["Average Sleep Duration (hrs)"].mean(), 2))

st.divider()

# Glucose over time
st.subheader("Glucose Trend Over Time")
fig1 = px.line(
    df_filtered,
    x="time",
    y="glucose",
    color="Patient_ID",
    title="Glucose Levels Over Time"
)
st.plotly_chart(fig1, use_container_width=True)

# Glucose distribution
st.subheader("Glucose Distribution")
fig2 = px.histogram(
    df_filtered,
    x="glucose",
    nbins=50,
    title="Distribution of Glucose Levels"
)
st.plotly_chart(fig2, use_container_width=True)

# Activity vs glucose
st.subheader("Activity vs Glucose")
fig3 = px.scatter(
    df_filtered,
    x="steps",
    y="glucose",
    color="Patient_ID",
    title="Steps vs Glucose"
)
st.plotly_chart(fig3, use_container_width=True)

# Insulin vs glucose
st.subheader("Bolus Insulin vs Glucose")
fig4 = px.scatter(
    df_filtered,
    x="bolus_volume_delivered",
    y="glucose",
    color="Patient_ID",
    title="Bolus Insulin Delivered vs Glucose"
)
st.plotly_chart(fig4, use_container_width=True)

# Sleep quality vs glucose
st.subheader("Sleep Quality vs Glucose")
fig5 = px.box(
    df_filtered,
    x="Sleep Quality (1-10)",
    y="glucose",
    title="Glucose by Sleep Quality"
)
st.plotly_chart(fig5, use_container_width=True)

# Demographics
st.subheader("Patient Demographics")

col5, col6 = st.columns(2)

with col5:
    fig6 = px.histogram(
        df_filtered,
        x="Age",
        title="Age Distribution"
    )
    st.plotly_chart(fig6, use_container_width=True)

with col6:
    fig7 = px.pie(
        df_filtered.drop_duplicates("Patient_ID"),
        names="Gender",
        title="Gender Distribution"
    )
    st.plotly_chart(fig7, use_container_width=True)

# Raw data
st.subheader("Filtered Data")
st.dataframe(df_filtered)
