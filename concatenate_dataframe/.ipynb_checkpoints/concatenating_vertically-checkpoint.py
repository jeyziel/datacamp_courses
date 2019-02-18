#%% Import Pandas
# https://www.somebits.com/~nelson/pandas-multiindex-slice-demo.html
import pandas as pd

#%% Create columns e an empty array
medal = ['bronze', 'silver', 'gold']
medals = []

#%% read datasets and append 
for medal_type in medal:

    file = "../datasets/medals/%s_top5.csv" %medal_type

    medal_df = pd.read_csv(file, index_col='Country')

    medals.append(medal_df)

#%% concatenate medals :  medals
medals = pd.concat(medals, keys=['bronze', 'silver', 'gold'])

#%% sort the entries of medal: medals_sorted
medals_sorted = medals.sort_index(level=0)

#%% Print the number of bronze medals won by german
print(medals_sorted.loc[('bronze', 'Germany')])

#%% Print data about silver medal
print(medals_sorted.loc['silver'])

#%% Create alias for pd.IndexSlice: idx
idx = pd.IndexSlice

##%% Print all the data on medals won by the United Kingdom
print(medals_sorted.loc[idx[:, 'United Kingdom'], ])

#%%Other way
print(medals_sorted.loc[(slice(None), 'United Kingdom'), :])