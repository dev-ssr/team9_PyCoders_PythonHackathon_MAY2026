import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# Set page config
st.set_page_config(page_title="Diabetes Analysis Dashboard", layout="wide")

# --- CUSTOM CSS: DARKER & LARGER TYPOGRAPHY ---
st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF; }
    
    /* MAIN TITLE - 70px Bold & Dark Navy */
    h1 { 
        font-size: 100px !important; 
        color: #0B243B !important; 
        text-align: center; 
        font-weight: 800 !important; 
        margin-bottom: 25px;
    }
    
    /* TARGETING THE TAB TEXT */
    .stTabs [data-baseweb="tab"] p {
        font-size: 70px !important; 
        font-weight: 700 !important;
        color: #0B243B !important;
        margin: 0 !important;
    }

    /* THE CONTAINER - Added margin-bottom for the highlight line */
    .stTabs [data-baseweb="tab"] {
        height: auto !important;
        padding-top: 20px !important;
        padding-bottom: 30px !important; /* Extra space for the line */
        margin-bottom: 10px !important;
    }

    /* FIXING THE HIGHLIGHT LINE (THE INDICATOR) */
    .stTabs [data-baseweb="tab-highlight"] {
        background-color: #EC7063 !important; /* Matches your pie chart red */
        height: 8px !important; /* Makes the line thicker and visible */
        bottom: 0px !important;
    }

    /* ENSURE THE TABS LIST DOESN'T HIDE THE LINE */
    .stTabs [role="tablist"] {
        gap: 50px !important;
        border-bottom: 2px solid #D5DBDB !important;
    }
    
    /* SECTION HEADERS (Descriptive/Prescriptive Analysis) - 45px Dark Slate */
    h2 { 
        font-size: 70px !important; 
        color: #17202A !important; 
        text-align: center; 
        font-weight: 700 !important; 
        margin-top: 35px; 
    }
    
    /* CHART TITLES - 32px Bold & Dark Slate */
    h3 { 
        font-size: 50px !important; 
        color: #1C2833 !important; 
        text-align: center; 
        font-weight: 700 !important; 
    }
    
    /* CAPTIONS - 24px Bold & Charcoal */
    .custom-caption {
        font-size: 45px !important;
        font-weight: 600 !important;
        color: #212F3D !important;
        text-align: center;
        margin-top: 20px;
        margin-bottom: 60px;
        line-height: 1.6;
    }

    /* KPI METRICS - Darker Text 
    [data-testid="stMetricLabel"] { font-size: 22px !important; font-weight: 800 !important; color: #0B243B !important; }
    [data-testid="stMetricValue"] { font-size: 36px !important; color: #1A5276 !important; font-weight: 800 !important; }*/
            
            /* TARGETING THE INNER DIV OF THE LABEL */
    # [data-testid="stMetricLabel"] > div { 
    #     font-size: 60px !important; /* Bumped to 30px for better visibility */
    #     font-weight: 800 !important; 
    #     color: #0B243B !important; 
    #     line-height: 1.2 !important;
    # }

    /* TARGETING THE INNER DIV OF THE VALUE */
    # [data-testid="stMetricValue"] > div { 
    #     font-size: 65px !important; /* Bumped to 45px */
    #     color: #1A5276 !important; 
    #     font-weight: 800 !important; 
    # }
            
            /* THE MAIN CONTAINER: Adding the border and centering content */
    [data-testid="metric-container"] {
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important; 
        justify-content: center !important;
        text-align: center !important;
        
        /* BORDER STYLING */
        border: 5px solid #0B243B !important; /* Dark Navy border */
        border-radius: 20px !important;
        padding: 30px !important;
        background-color: #FDFEFE !important;
        
        /* Ensures the box is big enough for 60px/65px fonts */
        min-height: 280px !important; 
        margin-bottom: 20px !important;
    }

    /* TARGETING THE LABEL TEXT */
    [data-testid="stMetricLabel"] > div { 
        font-size: 60px !important; 
        font-weight: 800 !important; 
        color: #0B243B !important; 
        line-height: 1.1 !important;
        margin-bottom: 10px !important;
    }

    /* TARGETING THE VALUE TEXT (The Numbers) */
    [data-testid="stMetricValue"] > div { 
        font-size: 65px !important; 
        color: #1A5276 !important; 
        font-weight: 900 !important; 
        line-height: 1.1 !important;
    }

    /* Chart Container Borders */
    [data-testid="stVerticalBlock"] > div:has(div.stPlotlyChart) {
        border: 7px solid #85929E;
        border-radius: 16px;
        padding: 35px;
        background-color: #FDFEFE;
    }

    [data-testid="metric-container"] {
        background-color: #FDFEFE;
        border: 3px solid #85929E;
        padding: 25px;
        border-radius: 16px;
    }
    </style>
    """, unsafe_allow_html=True)

@st.cache_data
def load_data():
    df = pd.read_csv("clean.csv")
    df['time'] = pd.to_datetime(df['time'])
    df['hour'] = df['time'].dt.hour
    return df

df = load_data()

# --- KPI CALCULATIONS ---
def glucose_category(glucose):
    if glucose < 140: return "Normal"
    elif glucose < 180: return "Prediabetic"
    else: return "Diabetic"

df["Glucose_Category"] = df["glucose"].apply(glucose_category)
total_patients = df["Patient_ID"].nunique()
avg_glucose = round(df["glucose"].mean(), 2)
avg_heart_rate = round(df["heart_rate"].mean(), 2)
avg_steps = round(df["steps"].mean(), 2)
avg_sleep = round(df["Average Sleep Duration (hrs)"].mean(), 2)
normal_glucose_percent = round((df[df["Glucose_Category"] == "Normal"].shape[0] / len(df)) * 100, 2)

# --- HEADER ---
st.markdown("<h1>Diabetes Analysis Dashboard</h1>", unsafe_allow_html=True)

kpi_col1, kpi_col2, kpi_col3, kpi_col4, kpi_col5, kpi_col6 = st.columns(6)
with kpi_col1: st.metric("👥 Total Patients", total_patients)
with kpi_col2: st.metric("🩸 Avg Glucose", avg_glucose)
with kpi_col3: st.metric("❤️ Avg Heart Rate", avg_heart_rate)
with kpi_col4: st.metric("👣 Avg Steps", avg_steps)
with kpi_col5: st.metric("😴 Avg Sleep", f"{avg_sleep} hrs")
with kpi_col6: st.metric("✅ Normal %", f"{normal_glucose_percent}%")

st.markdown("<br>", unsafe_allow_html=True)

# --- REFINED PLOT STYLING HELPER ---
def style_plot(fig, gap=0.2, m_size=None):
    fig.update_layout(
        height=800,
        template='plotly_white',
        bargap=gap,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=70, r=40, t=120, b=70),
        legend=dict(orientation="h", yanchor="bottom", y=1.05, xanchor="center", x=0.5, font=dict(size=40, color="#17202A")),
        xaxis=dict(showgrid=False, tickfont=dict(size=40, color="#17202A"), title_font=dict(size=40, color="#0B243B", weight="bold")),
        yaxis=dict(showgrid=False, tickfont=dict(size=40, color="#17202A"), title_font=dict(size=40, color="#0B243B", weight="bold"))
    )
    if m_size:
        fig.update_traces(marker=dict(size=m_size), selector=dict(type='scatter'))
    return fig

# --- TABS ---
tab1, tab2, tab3 = st.tabs(["Descriptive Analysis", "Prescriptive Analysis", "Predictive Analysis"])

with tab1:
    st.markdown("<h2>Descriptive Analysis</h2>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<h3>Average Glucose by Gender & Race</h3>", unsafe_allow_html=True)
        pivot_df = df.groupby(['Race', 'Gender'])['glucose'].mean().reset_index()
        fig1 = px.bar(pivot_df, x='Race', y='glucose', color='Gender', barmode='group', 
                      color_discrete_sequence=['#2E86C1', '#7FB3D5'])
        st.plotly_chart(style_plot(fig1), use_container_width=True)
        st.markdown("<p class='custom-caption'>Comparison of average glucose levels across demographic groups.</p>", unsafe_allow_html=True)

        
    
    with col2:
        st.markdown("<h3>Distribution of Glucose Levels</h3>", unsafe_allow_html=True)

        fig2 = px.histogram(
            df,
            x='glucose',
            nbins=30,
            color_discrete_sequence=['#2E86C1']
        )

        fig2.update_layout(
            title="Distribution of Glucose Levels",
            xaxis_title="Glucose",
            yaxis_title="Frequency"
        )

        st.plotly_chart(style_plot(fig2), use_container_width=True)

        st.markdown("<p class='custom-caption'>Frequency analysis of glucose readings across the patient population.</p>", unsafe_allow_html=True)

    col3, col4 = st.columns(2)
    with col3:
        st.markdown("<h3>Activity vs Heart Rate</h3>", unsafe_allow_html=True)
        fig3 = px.scatter(df.sample(min(len(df), 800)), x='steps', y='heart_rate', 
                          opacity=0.7, color_discrete_sequence=['#1F618D'])
        st.plotly_chart(style_plot(fig3, m_size=20), use_container_width=True)
        st.markdown("<p class='custom-caption'>Correlation between movement intensity and cardiovascular response.</p>", unsafe_allow_html=True)

    with col4:
        st.markdown("<h3>Average Basal Rate by Age Group</h3>", unsafe_allow_html=True)
        df['AgeGroup'] = pd.cut(df['Age'], bins=[0, 30, 45, 60, 100], labels=['<30', '30-45', '45-60', '60+'])
        age_basal = df.groupby('AgeGroup', observed=False)['basal_rate'].mean().reset_index()
        fig4 = px.bar(age_basal, x='AgeGroup', y='basal_rate', color_discrete_sequence=['#5D8AA8'])
        st.plotly_chart(style_plot(fig4, gap=0.6), use_container_width=True)
        st.markdown("<p class='custom-caption'>Trends in background insulin requirements across age brackets.</p>", unsafe_allow_html=True)

with tab2:
    st.markdown("<h2>Prescriptive Analysis</h2>", unsafe_allow_html=True)
    pcol1, pcol2 = st.columns(2)
    with pcol1:
        st.markdown("<h3>Sleep Impact on Hypo Frequency</h3>", unsafe_allow_html=True)
        night_df = df[df['hour'].between(0, 6)].copy()
        night_df['is_hypo'] = night_df['glucose'] < 70
        sleep_hypo = night_df.groupby('Patient_ID').agg(avg_s=('Average Sleep Duration (hrs)', 'mean'), h_f=('is_hypo', 'mean')).reset_index()
        fig5 = px.scatter(sleep_hypo, x='avg_s', y='h_f', trendline="ols", color_discrete_sequence=['#E67E22'])
        st.plotly_chart(style_plot(fig5, m_size=20), use_container_width=True)
        st.markdown("<p class='custom-caption'>Evaluating the relationship between rest duration and low glucose risks.</p>", unsafe_allow_html=True)

    with pcol2:
        st.markdown("<h3>Emergency Condition Mapping</h3>", unsafe_allow_html=True)
        alerts = df[(df['heart_rate'] > 100) & ((df['glucose'] < 70) | (df['glucose'] > 180))]
        fig6 = px.scatter(alerts.sample(min(len(alerts), 500)), x='heart_rate', y='glucose', 
                          color='glucose', color_continuous_scale='Bluered')
        st.plotly_chart(style_plot(fig6, m_size=20), use_container_width=True)
        st.markdown("<p class='custom-caption'>Combined high heart rate and glucose instability markers.</p>", unsafe_allow_html=True)
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