## FILE INDEX:

## 1. Team9_PyCoders_Category1.CleaningPreprocess.ipynb  
   - Category 1 queries  
   - Performs data cleaning, preprocessing, handling missing values, standardizing columns, merging raw files  
   - Generates the final clean dataset: clean.csv

## 2. Team9_PyCoders_Category2.Descriptive.ipynb  
   - Category 2 queries  
   - Summary statistics, distributions, univariate and bivariate analysis  
   - Uses clean.csv as input

## 3. Team9_PyCoders_Category3.PrescriptiveAnalysis_(1-15).ipynb  
   - Category 3 queries (Part 1)  
   - Covers prescriptive questions 1–15  
   - Generates rule-based insights and prescriptive logic  
   - Uses clean.csv as input

## 4. Team9_PyCoders_Category3.PrescriptiveAnalysis_(16-30).ipynb  
   - Category 3 queries (Part 2)  
   - Covers prescriptive questions 16–30  
   - Continues rule-based insights and recommendations  
   - Uses clean.csv as input

## 5. Team9_PyCoders_Category4.Predictive.ipynb  
   - Category 4 queries  
   - Predictive modeling, train/test split, evaluation metrics  
   - Uses clean.csv as input

## 6. load_dataset.ipynb  
   - Loads and explores raw data  
   - Initial inspection before cleaning  
   - Used before creating merged_data.csv

## 7. app.py  
   - Streamlit dashboard  
   - Visualizes insights using clean.csv  
   - Runs locally from command prompt

## 8. Team9_PyCoders_clean.csv  
   - Final cleaned, standardized, and analysis-ready dataset  
   - Output from Category 1 notebook  
   - Used in Category 2, 3, 4 notebooks and Streamlit dashboard

## Source files:

1. HUPA-UC Diabetes Dataset/  
   - Raw source folder containing original patient-level and visit-level files  
   - Used to create merged_data.csv and clean.csv

## Dashboard:

This project uses a Streamlit dashboard built in `app.py`.

## How to run the dashboard locally:
1. Install required packages:  
   pip install -r requirements.txt

2. Run the Streamlit app:  
   streamlit run app.py

3. The dashboard will open automatically in your browser at: 
   http://localhost:8501

## Notes:
- The dashboard uses `clean.csv` as the primary dataset.  
- Ensure `clean.csv` is in the same directory as `app.py` before running.

