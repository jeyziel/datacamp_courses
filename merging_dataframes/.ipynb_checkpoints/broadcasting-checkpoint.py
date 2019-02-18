#%% import Pandas
import pandas as pd

#%% read csv
weather = pd.read_csv('../datasets/pittsburgh2013.csv')
weather.head()

#%% extract selected columns from weather as a new DataFrame
temps_f = weather[['Min TemperatureF', 'Mean TemperatureF', 'Max TemperatureF']]

#%% convert temps_f to celsius :
temps_c = (temps_f - 32) * 5/9

#%% Rename 'F' in column names with 'C': 
temps_c.columns = temps_c.columns.str.replace('F', 'C')
temps_c.head()




