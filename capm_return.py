# -*- coding: utf-8 -*-

import pandas as pd
import streamlit as st
import yfinance as yf
import datetime
from dateutil.relativedelta import relativedelta
import pandas_datareader.data as web


# Set up the Streamlit page configuration
st.set_page_config(
    page_title = "CAPM",
    page_icon = "chart_with_upwards_trend",
    layout ="wide"
)

# Title and header
st.title("Capital Asset Pricing Model (CAPM)")


# Getting input from user
col1, col2 = st.columns([1, 1])
with col1:
    stock_list = st.multiselect("Select 4 Stocks", ('TSLA','AAPL', 'NFLX', 'MSFT', 'MGM', 'AMZN', 'GOOGL'), ['TSLA','AAPL', 'AMZN', 'GOOGL'])
with col2:
    year = st.number_input("Number of years", 1, 10)


# downloading data for SP500

# Get today's date (end date)
end_date = datetime.date.today()

# Calculate the start date by subtracting the number of years using relativedelta
start_date = end_date - relativedelta(years=year)

# fetching sp500 data
SP500 = web.DataReader(['sp500'], 'fred', start_date, end_date) #  sp500 refers to the specific series or dataset, 
# The term fred in the line of code you provided refers to Federal Reserve Economic Data (FRED), which is an online database of economic 
# data maintained by the Federal Reserve Bank of St. Louis. The FRED database contains a wealth of macroeconomic 
# and financial data, including data on interest rates, inflation, employment, GDP, and more.


# Fetch historical stock data for companies in stock_list 
stocks_df = pd.DataFrame()

for stock in stock_list:
    data = yf.download(stock, period=f'{year}y')
    stocks_df[f'{stock}'] = data['Close']

# add an index to avoid using data as an index in both dataframe
SP500.reset_index(inplace=True)
stocks_df.reset_index(inplace=True)

# rename the SP500 DATE column to Date to match the stocks_df
SP500.columns = ['Date', 'SP500']

# merge the SP500 to stocks_df
stocks_df = pd.merge(stocks_df, SP500, on='Date', how='inner')


# make a column for the head() and tail() of stocks_df
col1, col2 = st.columns([1,1])
with col1:
    st.markdown("### Dataframe head")
    st.dataframe(stocks_df.head(), use_container_width=True)
with col2:
    st.markdown("### Dataframe tail")
    st.dataframe(stocks_df.tail(), use_container_width=True)



