import pandas as pd
import streamlit as st
import yfinance as yf
import datetime
from dateutil.relativedelta import relativedelta
import pandas_datareader.data as web
import capm_functions


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
    tech_stock_list = st.multiselect("Select 4 Stocks", 
                                ('AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA', 'NVDA', 'META', 'ADBE', 'INTC', 'ORCL'), 
                                ['META','AAPL', 'AMZN', 'GOOGL'])
with col2:
    year = st.number_input("Number of years", 1, 10)


# Get today's date (end date) and calculate the start date
end_date = datetime.date.today()
start_date = end_date - relativedelta(years=year)


# Fetch SP500 data and stock data simultaneously
stocks_df = yf.download(tech_stock_list + ['^GSPC'], start=start_date, end=end_date)['Adj Close']
stocks_df.columns = tech_stock_list + ['SP500']
print(stocks_df.head())

# Reset the index so 'Date' becomes a column instead of an index
stocks_df.reset_index(inplace=True)

# Fill missing values forward or drop NaNs (depending on your preference)
stocks_df.ffill(inplace=True)


# Display head and tail of the DataFrame
col1, col2 = st.columns([1, 1])
with col1:
    st.markdown("### Dataframe head")
    st.dataframe(stocks_df.head(), use_container_width=True)
with col2:
    st.markdown("### Dataframe tail")
    st.dataframe(stocks_df.tail(), use_container_width=True)


# Interactive plot of the stocks and normalized stocks
col1, col2 = st.columns([1, 1])
with col1:
    st.markdown("### `Price of all stocks`")
    st.plotly_chart(capm_functions.interactive_plot(stocks_df))
with col2:
    st.markdown("### `Price of all stocks after normalization`")
    st.plotly_chart(capm_functions.interactive_plot(capm_functions.normalize(stocks_df)))


# Calculate daily returns
stocks_daily_return = capm_functions.daily_return(stocks_df)


# Calculate beta and alpha for each stock
beta, alpha = {}, {}
for stock in tech_stock_list:
    b, a = capm_functions.calculate_beta(stocks_daily_return, stock)
    beta[stock] = round(b, 4)
    alpha[stock] = round(a, 4)



# Display calculated beta values
beta_df = pd.DataFrame(list(beta.items()), columns=['Stock', 'Beta Value'])
with col1:
    st.markdown('### `Calculated Beta Value`')
    st.dataframe(beta_df, use_container_width=True)


# Calculate expected returns using CAPM
rf = 0  # Risk-free rate
rm = stocks_daily_return['SP500'].mean() * 252  # Expected market return (annualized)

# Calculate return values and store them in DataFrame
return_df = pd.DataFrame({
    'Stock': tech_stock_list,
    'Return Value': [f"{round(rf + beta[stock] * (rm - rf), 2):.2f}" for stock in tech_stock_list]
})


with col2:
    st.markdown('### `Calculated Return using CAPM `')
    st.dataframe(return_df, use_container_width=True)















# Solving for beta using the covariance approach

cov_matrix = stocks_daily_return.cov()
print(cov_matrix) 


# Calculate the variance of the market (S&P 500)
market_variance = stocks_daily_return['SP500'].var()

# Define the list of stocks you're interested in
stocks = ['META','AAPL', 'AMZN', 'GOOGL']

# Initialize a dictionary to store beta values
beta_covariance = {}

# Calculate beta for each stock
for stock in stocks:
    # Extract the covariance between the stock and the market (SP500)
    cov_stock_market = cov_matrix.loc[stock, 'SP500']
    
    # Calculate the beta
    beta_covariance[stock] = float(round(cov_stock_market / market_variance, 4))


print(beta_covariance)