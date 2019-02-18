
#%% Import Pandas
import pandas as pd

#%%[markdown]
# ##This job in this exercice is to compute yearly percet-change of US GDP

#%% Read GDP USA
gdp = pd.read_csv('datasets/GDP/gdp_usa.csv', parse_dates=True, index_col='DATE')
print(gdp.head())
#%% Slice all the GDP data from 2008 onward
pos2018 = gdp.loc['2008':]

#%% Resample post2008 by year, keeping last(): yearly
yearly = pos2018.resample('A').last()
print(yearly.head())

#%% Compute percentage growth of yearly: yearly['growth']
yearly['growth'] = yearly.pct_change() * 100

#%% print yearly again
print(yearly.head())


