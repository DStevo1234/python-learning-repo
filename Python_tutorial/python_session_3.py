# name = 'Will'
# num_1 = 1
# num_2 = 1.0
# list_1 = ['item1','item2','item3']
# dict_1 = ['key1':'value1'
#           'key2':'value2']

import pandas as pd

# List of Dicts - each dist is a row, with keys being column names
# Dict of list - each key:value pair is a column

# df_1 = pd.DataFrame([
#    {'Col1':1,
#     'Col2':2,
#     'Col3':3},
#     {'Col1':'A',
#      'Col2':'B',
#     'Col3':'C'}
# ])

# filename = 'https://raw.githubusercontent.com/data-to-insight/ERN-sessions/main/data/1980%202023%20average%20house%20prices.csv'
# df = pd.read_csv(filename)

# df['Period'] = pd.to_datetime(df['Period'], format='%Y-%m')

# print(df.info())

# df['Age of Data(Years)'] = pd.to_datetime('today').normalize() - df['Period']

# df['Age of Data(Years)'] = df['Age of Data(Years)']/pd.Timedelta('365 days')

# df['Age of Data(Years)'] = df['Age of Data(Years)'].astype('int')

# print(df['Age of Data(Years)'])

filename_2 = 'https://raw.githubusercontent.com/data-to-insight/ERN-sessions/main/data/ChildIdentifiers.csv'

df = pd.read_csv(filename_2)

df['PersonBirthDate'] = pd.to_datetime(df['PersonBirthDate'], format = '%Y-%m-%d', errors='coerce')

df['Age'] = pd.to_datetime('today').normalize() - df['PersonBirthDate']

df['Age'] = df['Age']/pd.Timedelta('365 days')

df['Age'] = df['Age'].astype('int')

# == equals
# &/and - symbols act row by row, word column by column
# |/or - symbols act row by row, word column by column
# .isin([1,2]) - 1 or 2
# ~ - is not


# max_age = df['Age'].max()

# min_age = df['Age'].min()

# mean_age =  df['Age'].mean()

# print(f'max: {max_age}, min: {min_age}, mean: {mean_age}')

# under_15_condition = df['Age'] < 15

# under_15 = df[under_15_condition]

# print(under_15)

# condition = (df['Age'] < 15) & (df['GenderCurrent'].isin([0,9]))

# sliced_df = df[condition]

# print(sliced_df)

# .map() - convert values to another
# .str.lower() - change the capitilsation of strings

df['GenderCurrent'] = df['GenderCurrent'].map({1:'Male',
                                                2:'Female',})

print(df['GenderCurrent'])