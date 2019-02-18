#%% Import Pandas
import pandas as pd

#%% Read Jan Units Sales
jan_units = pd.read_csv('datasets/Sales/sales-jan-2015.csv', parse_dates=True, index_col='Date')

#%% Read Feb Units Sales
feb_units = pd.read_csv('datasets/Sales/sales-feb-2015.csv', parse_dates=True, index_col='Date')

#%% Read Mar Units Sales
mar_units = pd.read_csv('datasets/Sales/sales-mar-2015.csv', parse_dates=True, index_col='Date')

#%% append months
units = []
for month in [jan_units, feb_units, mar_units]:
    units.append(month['Units'])

quarter1 = pd.concat(units, axis='rows')

#%%Print slice for quart1 
# #jan 27, 2015 to feb 2,2015
# #feb 26, 2015 to mar 7,2015
print(quarter1.loc['jan 27, 2015' : 'feb 2, 2015'])
print(quarter1.loc['feb 26, 2015' : 'feb 26, 2015'])

print('Total UNits : ', quarter1.sum())