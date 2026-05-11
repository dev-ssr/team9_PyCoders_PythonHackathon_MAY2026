import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
df = pd.read_csv("clean.csv")
st.title("📊 HUPA-UC Diabetes Dashboard")
st.subheader("CGM + Sleep + Activity Analysis")
st.write("### Dataset Preview")
st.dataframe(df)
filtered_df = df.copy()

fig = px.scatter(
    filtered_df,
    x="Age",
    y="glucose",
    color="Gender"
)

st.plotly_chart(fig)