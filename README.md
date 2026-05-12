# Team9 PyCoders — Python Hackathon Project
# Project Overview

This repository contains a health data analytics project built for the Python Hackathon (May 2026).
It focuses on analyzing Continuous Glucose Monitoring (CGM) data to detect patterns, identify risk levels, and generate actionable insights for personalized healthcare.

# The project combines:

- Descriptive Data Analysis
- Risk Pattern Detection
- Personalized Patient Insights
- Data Visualization using Python

# Objective

## To analyze patient health data and identify:

- High glucose risk patterns
- Time-based (hourly) glucose fluctuations
- Patient-level risk exposure
- Relationships between lifestyle factors and glucose levels

 📁 Project Structure
- HUPA dataset → raw data source
- merged_data.csv → processed dataset
- clean.csv → cleaned dataset
- notebooks → EDA + analysis work
- app.py → Streamlit dashboard

 ## Tech Stack
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Streamlit

# How to Run the Project
Follow these steps to run `app.py` locally:
## Step 1: Clone the Repository
```bash
git clone <repository-url>
cd <project-folder>

## Step 2: Create a Virtual Environment (Optional but Recommended)
python -m venv venv
Activate Virtual Environment
Windows
venv\Scripts\activate
Mac/Linux
source venv/bin/activate

## Step 3: Install Required Libraries
pip install pandas numpy matplotlib seaborn streamlit jupyter

## Step 4: Run Jupyter Notebook (for analysis)
jupyter notebook
Open the notebook:
Team9_PyCoders_Category2.Descriptive analysis.ipynb

## Step 5: Run Streamlit Dashboard
streamlit run app.py

## tep 6: Open Dashboard in Browser
After running Streamlit, open:
http://localhost:8501

The dashboard will automatically launch in your browser.

## Key Insights
- Certain hours show high glucose risk spikes
- Risk varies significantly across patients
- Personalized risk scoring improves prediction accuracy
- streamlit run app.py 
