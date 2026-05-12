## FILE INDEX:

## 1. Charts
   - Contains images for the dashboard
     
## 2. HUPA-UC Diabetes Dataset
   -  Raw data set which has been cleaned and analyzed
   -  https://data.mendeley.com/datasets/3hbcscwz44/1

## 3. Team9_PyCoders_Category1.CleaningPreprocess.ipynb  
   - Category 1 queries  
   - Performs data cleaning, preprocessing, handling missing values, standardizing columns, merging raw files  
   - Generates the final clean dataset: Team9_PyCoders_clean.csv

## 4. Team9_PyCoders_Category2.Descriptive.ipynb  
   - Category 2 queries  
   - Summary statistics, distributions, univariate and bivariate analysis  
   - Uses Team9_PyCoders_clean.csv as input

## 5. Team9_PyCoders_Category3.PrescriptiveAnalysis_(1-15).ipynb  
   - Category 3 queries (Part 1)  
   - Covers prescriptive questions 1–15  
   - Generates rule-based insights and prescriptive logic  
   - Uses Team9_PyCoders_clean.csv as input

## 6. Team9_PyCoders_Category3.PrescriptiveAnalysis_(16-30).ipynb  
   - Category 3 queries (Part 2)  
   - Covers prescriptive questions 16–30  
   - Continues rule-based insights and recommendations  
   - Uses Team9_PyCoders_clean.csv as input

## 7. Team9_PyCoders_Category4.Predictive.ipynb  
   - Category 4 queries  
   - Predictive modeling- Comparing different models to answer the question "Can we predict future glucose values?"
   - Uses Team9_PyCoders_clean.csv as input

## 8. load_dataset.ipynb  
   - Loads and explores raw data  
   - Initial inspection before cleaning  
   - Used before creating merged_data.csv

## 9. Team9_PyCoders_app.py  
   - Streamlit dashboard  
   - Visualizes insights using Team9_PyCoders_clean.csv
   - Runs locally from command prompt

## 10. Team9_PyCoders_clean.csv  
   - Final cleaned, standardized, and analysis-ready dataset  
   - Output from Category 1 notebook  
   - Used in Category 2, 3, 4 notebooks and Streamlit dashboard 
- Ensure `clean.csv` is in the same directory as `app.py` before running.

