#import pandas
#%%
import pandas as pd

#%% create a list of dataframe list
filenames = ['Gold.csv', 'Silver.csv', 'Bronze.csv']

#%% Create a list of three Dataframe: dataframes
dataframes = []
for filename in filenames:
    dataframes.append(pd.read_csv('datasets/medals/' + filename))

#%%
# Make a copy of Gold Medal
medals = dataframes[0].copy()

#%%
#Create a list of new column names
new_labels = ['NOC', 'Country', 'Gold']


#%% Rename the columns of medals using new_labels
medals.column = new_labels

#%% Add columns "silver" and "bronze" for medal
medals['silver'] = dataframes[1]['Total']
medals['bronze'] = dataframes[2]['Total']

#%% print medal
print(medals.head())