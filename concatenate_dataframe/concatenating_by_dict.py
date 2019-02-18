#%% Import pandas
import pandas as pd

#%% read csv files
months = ['jan', 'feb', 'mar']
sales_dict = {}

for month  in months:
    file = "datasets/Sales/sales-%s-2015.csv" % month
    df_sales = pd.read_csv(file, parse_dates = True)
    sales_dict[month] = df_sales.groupby('Company').sum()

#%% concatenate files
sales_month = pd.concat(sales_dict)
print(sales_month.head())

#%%Print all sales by mediacore
idx = pd.IndexSlice
print(sales_month.loc[idx[:, 'Mediacore'], :])