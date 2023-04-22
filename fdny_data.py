import pandas as pd #to import the requried module (pandas)
#import the file
df_fdny_csv_raw = pd.read_csv("FDNY.csv")
#view the statistics using describe
print(df_fdny_csv_raw.describe)
#view first 5 rows
print(df_fdny_csv_raw.head())
df_fdny_csv_data = pd.read_csv("FDNY.csv",skiprows=1)
print(df_fdny_csv_data.head(5))
#view statistics
print(df_fdny_csv_data.describe())
#view the columns
print(df_fdny_csv_data.columns)
#view the index
print(df_fdny_csv_data.index)
#count number of records
print(df_fdny_csv_data.count())
#groupby borough column
get_groupby_borough = df_fdny_csv_data.groupby('Borough')
#view the size
print(get_groupby_borough.size())
#get the manhattan borough data
file_info_manhattan = get_groupby_borough.get_group('Manhattan')
#view the first 5 rows of the data
print(file_info_manhattan.head())