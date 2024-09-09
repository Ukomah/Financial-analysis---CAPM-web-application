import plotly.express as px
import numpy as np


# function to plot interactive plotly chart
def interactive_plot(df):
    fig = px.line()
    for i in df.columns[1:]:
        fig.add_scatter(x = df['Date'], y=df[i], name=i)
    fig.update_layout(
        width=550,
        margin=dict(l=20, r=20, t=50, b=20),
        legend=dict(orientation='h', yanchor='bottom', y=1.2, xanchor='right', x=1,)
        )
    
    return fig


# function to normalize the pricess based on the initial price
def normalize(df):
    # Make a copy of the dataframe to avoid modifying the original
    df_normalized = df.copy()

    # Normalize all columns except the 'Date' column
    df_normalized[df.columns[1:]] = df[df.columns[1:]].div(df.iloc[0][1:])

    return df_normalized


# function to calculate daily returns
def daily_return(df):

    # Make a copy of the dataframe to avoid modifying the original
    df_dreturns = df.copy()

    # Loop through all columns except the first one
    for i in df_dreturns.columns[1:]:
        # Calculate daily returns using Pandas shift method
        df_dreturns[i] = df_dreturns[i].pct_change() * 100  # Calculates percentage change from previous row
        
    # Replace NaN (first row) with 0 because there's no return on the first day
    df_dreturns.fillna(0, inplace=True)
    
    return df_dreturns


# function to calculate beta
def calculate_beta(stocks_daily_return, stock):

    # fitting a linear regression usinf np.polyfit
    b, a = np.polyfit(stocks_daily_return['SP500'], stocks_daily_return[stock], 1)

    # return beta and alpha
    return b, a
