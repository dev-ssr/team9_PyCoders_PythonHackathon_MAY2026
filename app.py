import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os

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
    csv_path = os.path.join(os.path.dirname(__file__), "clean.csv")
    df = pd.read_csv(csv_path)
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
    import os
    plot_dir = "./analysis_plots/prescriptive_analysis/"

    # Question 1
    st.markdown(f'<div style="font-weight: bold; font-size: 22px;">1. How can multi-source wearable and CGM data be used to build a patient-level prescriptive risk scoring system for Type 1 Diabetes that identifies high-risk individuals and recommends personalized intervention strategies?</div>', unsafe_allow_html=True)
    q1_plots = ["Top 10 High-Risk Patients.png", "Patient Risk Category Distribution.png", "Risk Category by Age Group.png", "Average Risk Score by Age Group.png"]
    q1_existing = [p for p in q1_plots if os.path.exists(os.path.join(plot_dir, p))]
    if q1_existing:
        cols = st.columns(len(q1_existing))
        for idx, p in enumerate(q1_existing):
            with cols[idx]:
                st.image(os.path.join(plot_dir, p), use_container_width=True)
    st.info("""The model identifies a clear subgroup of high-risk T1DM patients with elevated risk scores driven by glucose instability, frequent hyper/hypoglycemic events, and physiological stress indicators. A large portion of patients fall into the High Risk category, suggesting significant variability in disease control across individuals. Moderate and low-risk groups indicate relatively better glucose stability and healthier lifestyle patterns. Overall, diabetes risk in this cohort is strongly influenced by combined effects of glucose dynamics, heart rate stress, and behavioral factors like sleep and activity.\n\n\n### Prescriptive Insights \n#### 1. For High-Risk Patients:\n##### Observed:\nHigh glucose variability\nFrequent hyper/hypoglycemia\nElevated heart rate stress\nPoor sleep + low activity\n##### Recommended actions:\nAdjust insulin timing and dosing\nContinuous glucose monitoring alerts\nImprove sleep hygiene (fixed sleep schedule)\nIncrease moderate physical activity\nStress management interventions\n#### 2.For Moderate-Risk Patients:\n##### Observed:\nOccasional glucose spikes\nPartial lifestyle imbalance\n##### Recommended actions:\nMonitor post-meal glucose trends\nImprove activity consistency\nSleep tracking optimization\n#### 3.For Low-Risk Patients:\n##### Observed:\nStable glucose patterns\nBalanced lifestyle metrics\n##### Recommended actions:\nMaintain current routine\nPreventive monitoring only""")

    # Question 7
    st.markdown(f'<div style="font-weight: bold; font-size: 22px;">7. How can time-of-day glucose patterns and patient-level behavior be combined to develop a risk exposure model that classifies patients into actionable sensitivity levels for personalized Diabetes management?</div>', unsafe_allow_html=True)
    if os.path.exists(os.path.join(plot_dir, "plot.png")):
        cols = st.columns(2)
        with cols[0]:
            st.image(os.path.join(plot_dir, "plot.png"), use_container_width=True)
        with cols[1]:
            st.image(os.path.join(plot_dir, "plot.png"), use_container_width=True)
    st.info("""The global pattern shows that 11 AM and 7\u201310 PM are the most consistent high\u2011risk glucose hours, meaning these windows are when glucose tends to run highest across the entire population.\nPatients with the highest personal risk exposure ratios (e.g., HUPA0010P, HUPA0022P, HUPA0027P) spend a large proportion of their readings inside these high\u2011risk hours, indicating that their daily routines place them directly in the time windows where glucose is most unstable.\nPatients with higher personal risk exposure are likely more sensitive to circadian glucose fluctuations, especially during evening hours. These individuals may require stricter monitoring and optimized insulin timing during identified high-risk periods.""")

    # Question 12
    st.markdown(f'<div style="font-weight: bold; font-size: 22px;">12. Does average sleep duration directly influence the frequency of dangerous nocturnal hypoglycemia? Is there a \'safe\' sleep duration threshold below which overnight hypoglycemia frequency significantly increases?</div>', unsafe_allow_html=True)
    if os.path.exists(os.path.join(plot_dir, "Sleep Duration vs Nocturnal Hypo Frequency.png")):
        st.image(os.path.join(plot_dir, "Sleep Duration vs Nocturnal Hypo Frequency.png"))
    st.info("""The regression analysis identifies the correlation between sleep length and the prevalence of overnight lows. For short sleepers, prescribe higher bedtime glucose targets or a reduction in nocturnal basal rates.""")

    # Question 18
    st.markdown(f'<div style="font-weight: bold; font-size: 22px;">18. Should alerts be triggered when heart rate and glucose simultaneously become abnormal?</div>', unsafe_allow_html=True)
    if os.path.exists(os.path.join(plot_dir, "Potential Alert Conditions.png")):
        st.image(os.path.join(plot_dir, "Potential Alert Conditions.png"))
    st.info("""Many patients show extremely high glucose levels (180\u2013400) combined with elevated heart rates.\nA second cluster appears at low glucose levels (40\u201370), which may indicate hypoglycemia risk.\nHigher heart rates are observed in both hyperglycemic and hypoglycemic conditions.\nSeveral outlier patients show very high heart rate with abnormal glucose values, indicating possible emergency conditions.""")

    # Question 19
    st.markdown(f'<div style="font-weight: bold; font-size: 22px;">19. Can personalized treatment recommendations be created using combined physiological markers?</div>', unsafe_allow_html=True)
    if os.path.exists(os.path.join(plot_dir, "Multivariable Correlation Matrix.png")):
        st.image(os.path.join(plot_dir, "Multivariable Correlation Matrix.png"))
    st.info("""The multivariable correlation analysis revealed strong relationships between physical activity biomarkers such as steps and calories burned, while glucose showed weak direct correlation with individual biomarkers, including insulin delivery. These findings suggest that glucose regulation is highly multifactorial and influenced by complex interactions among activity, metabolism, insulin response, and patient-specific physiological factors. The results support the need for personalized, multi-factor diabetes monitoring and predictive healthcare systems.""")

    # Question 24
    st.markdown(f'<div style="font-weight: bold; font-size: 22px;">24. Should calorie expenditure be used to recommend insulin dosage changes?</div>', unsafe_allow_html=True)
    if os.path.exists(os.path.join(plot_dir, "Calories vs Future Glucose.png")):
        st.image(os.path.join(plot_dir, "Calories vs Future Glucose.png"))
    st.info("""Our analysis found that calorie expenditure alone had almost no correlation with glucose levels or insulin delivery. This suggests that insulin recommendations should not rely solely on calories burned. Instead, diabetes management may require combining multiple physiological indicators such as glucose trends, insulin dosage, activity intensity, and heart rate for more personalized treatment decisions.""")

    # Question 30
    st.markdown(f'<div style="font-weight: bold; font-size: 22px;">30. What combined intervention (steps + carb reduction + insulin review) should be recommended for participants with multiple risk indicators?</div>', unsafe_allow_html=True)
    if os.path.exists(os.path.join(plot_dir, "plot.png")):
        st.image(os.path.join(plot_dir, "plot.png"))
    st.info("""\u201cUrgent\u201d cases show the worst combination:\n      - very low steps\n      - very high carb intake\n      - high insulin dosing\n\u2022 \u201cModerate\u201d cases show early warning signs:\n      - slightly low activity OR\n      - moderately high carb intake\n\u2022 \u201cMaintain\u201d group represents stable lifestyle behavior.\n\u2022 Bubble size (insulin volume) highlights individuals with heavy insulin reliance.\n\u2022 This visualization quickly identifies who needs immediate lifestyle intervention.""")
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

    charts_dir = os.path.join(os.path.dirname(__file__), "charts")
    linear_img = Image.open(os.path.join(charts_dir, "linear_regression.png"))
    xgb_img = Image.open(os.path.join(charts_dir, "xgboost.png"))
    lstm_img = Image.open(os.path.join(charts_dir, "lstm.png"))
    gru_img = Image.open(os.path.join(charts_dir, "gru.png"))

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