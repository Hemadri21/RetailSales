
import streamlit as st
import pandas as pd

st.set_page_config(layout='wide', page_title='Retail Sales Dashboard')
st.title('Retail Sales Prediction & Dashboard')

st.markdown('Upload `RetailSales.csv` if not already present in the working directory.')

def load_csv(uploaded):

    if uploaded is not None:
        try:
            return pd.read_csv(uploaded)
        except Exception as e:
            st.error(f"Failed to read the uploaded file: {e}")
            return None
    try:
        return pd.read_csv('RetailSales.csv')
    except FileNotFoundError:
        st.error('No dataset found. Please upload RetailSales.csv.')
        st.stop()
    except Exception as e:
        st.error(f'Error reading RetailSales.csv: {e}')
        st.stop()

uploaded = st.file_uploader('Upload CSV', type=['csv'])
df = load_csv(uploaded)


if df is None:
    st.error("Dataframe wasn't loaded. Please upload RetailSales.csv or check the file format.")
    st.stop()


required = ['Date', 'Total_Sales']
missing = [c for c in required if c not in df.columns]
if missing:
    st.error(f"Missing required columns: {missing}. Found columns: {list(df.columns)}")
    st.stop()


df['Date'] = pd.to_datetime(df['Date'].astype(str), dayfirst=True, errors='coerce')
if df['Date'].isna().all():
    st.warning("All 'Date' values could not be parsed. Check the date format in your CSV.")
df['Total_Sales'] = pd.to_numeric(df['Total_Sales'], errors='coerce')

st.sidebar.header('Controls')
view = st.sidebar.selectbox('View', ['Sales Trend','Category Insights','Forecast'])


df = df.dropna(subset=['Date', 'Total_Sales'])
df = df.sort_values('Date')

if view == 'Sales Trend':
    st.subheader('Daily Sales Trend')
    daily = df.set_index('Date').resample('D')['Total_Sales'].sum().fillna(0)
    st.line_chart(daily)

    st.subheader('Monthly Sales')
    monthly = daily.resample('M').sum()
    st.bar_chart(monthly)

elif view == 'Category Insights':
    st.subheader('Category total sales')
    cat = df.groupby('Category')['Total_Sales'].sum().sort_values(ascending=False)
    st.bar_chart(cat)

    st.subheader('Top products')
    top = df.groupby('Product_Name')['Total_Sales'].sum().sort_values(ascending=False).head(10)
    st.table(top)

else:
    st.subheader('Forecast (precomputed if available)')
    try:
        fc = pd.read_csv('forecast.csv', index_col=0, parse_dates=True)
        st.line_chart(fc['Forecast'])
        st.write(fc.head())
    except Exception:
        st.info('No forecast file found. Run the notebook to generate forecast.csv')
