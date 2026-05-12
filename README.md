# Team9 PyCoders — Python Hackathon Project
# Project Overview

This repository contains a health data analytics project built for the Python Hackathon (May 2026).
It focuses on analyzing Continuous Glucose Monitoring (CGM) data to detect patterns, identify risk levels, and generate actionable insights for personalized healthcare.

# The project combines:

- Descriptive Data Analysis
- Prescriptive Data Analysis
- Predictive Data Analysis
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
- Team9_PyCoders_clean.csv → cleaned dataset
- notebooks → EDA + analysis work
- Team9_PyCoders_app.py → Streamlit dashboard

 ## Tech Stack
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Streamlit
- TensorFlow
- Scikit learn
  
# How to Run the Project
Follow these steps to run `Team9_PyCoders_app.py` locally:

---

# Step 1: Clone the Repository

```bash
git clone <repository-url>
cd <team9_PyCoder_PhythonHackthon_MAY2026>
```

# Step 2: Install Required Libraries

```bash
pip install pandas numpy matplotlib seaborn streamlit jupyter
```

---

# Step 3: Run Jupyter Notebook (for Analysis)

```bash
jupyter notebook
```

Open the notebook:

```text
Team9_PyCoders_app.py
```

---

# Step 4: Run Streamlit Dashboard

```bash
streamlit run Team9_PyCoders_app.py
```

---

# Step 5: Open Dashboard in Browser(Recommanded to open in Microsoftedge) 

After running Streamlit, open:

```text
http://localhost:8501
```

The dashboard will automatically launch in your browser.

## Key Insights
- Certain hours show high glucose risk spikes
- Risk varies significantly across patients
- Personalized risk scoring improves prediction accuracy
- streamlit run app.py 
