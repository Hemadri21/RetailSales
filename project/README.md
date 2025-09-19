
# Retail Sales Prediction & Dashboard - Internship Submission

Files included:
- `Retail_Sales_Project.ipynb` : Jupyter notebook with EDA and forecasting.
- `app.py` : Streamlit dashboard to view trends, category insights, and forecast (uses `forecast.csv`).
- `forecast.csv` : Generated when running the notebook (not included by default).
- `requirements.txt` : Python packages required.

How to use:
1. Place `RetailSales.csv` in the same folder or upload it via the Streamlit app.
2. (Optional) Run the notebook to generate `forecast.csv` (forecast saved to `/mnt/data/forecast.csv`).
3. To run the dashboard: `streamlit run app.py`

Notes:
- The notebook tries to use Prophet if available; otherwise it falls back to SARIMAX from statsmodels.
- If you want, I can also run the notebook and include `forecast.csv` for you. But I avoided running heavy model training to keep the submission lightweight.
