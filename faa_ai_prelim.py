import pandas as pd #to import the required module (pandas)
#import the file
df_faa_dataset = pd.read_csv("faa_ai_prelim.csv")
#view the shape
print(df_faa_dataset.shape)
#view first 5 rows
print(df_faa_dataset.head())
#view the columns
print(df_faa_dataset.columns)
#select the required columns
df_faa = df_faa_dataset[['ACFT_MAKE_NAME','LOC_STATE_NAME', 'ACFT_MODEL_NAME', 'RMK_TEXT',  'FLT_PHASE',
'EVENT_TYPE_DESC', 'FATAL_FLAG']]
#view the data type
print(type(df_faa))
#view first 5 rows
print(df_faa.head())
#check for empty cells in fatal flag column and replace with No
df_faa['FATAL_FLAG'].fillna(value='No', inplace=True)
#view first 5 rows
print(df_faa.head())
#view the shape
print(df_faa.shape)
#drop empty cells in the selected column
df_final = df_faa.dropna(subset=['ACFT_MAKE_NAME'])
#view the shape
print(df_final.shape)
#groupby aircraft type
aircrafttype = df_final.groupby('ACFT_MAKE_NAME')
#view the size
print(aircrafttype.size())
#groupby fatal size
fatalsize = df_final.groupby('FATAL_FLAG')
#view the size
print(fatalsize.size())
#get the group witht the Yes
fatalaccidents = fatalsize.get_group('Yes')
#view the data
print(fatalaccidents)
#fatalaccidents.to_csv('fatal accidents')
