#%% Import Pandas
import pandas as pd

#%% Read 'sp500.csv' into a DataFrame: sp500
sp500 = pd.read_csv('../datasets/sp500.csv', parse_dates=True, index_col='Date')
print(sp500.head())

#%% Read 'Exchange.csv' into a DataFrame: exchange
exchange = pd.read_csv('datasets/exchange.csv', parse_dates=True, index_col='Date')
print(exchange.head())

# Subset 'Open' & 'Close' columns from sp500: dollars
dollars = sp500[['Open', 'Close']]
print(dollars.head())

# Convert Dollar to Pound
pounds = dollars.multiply(exchange['GBP/USD'], axis='rows')
print(pounds.head())