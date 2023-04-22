import pandas as pd
import numpy as np

# series from a list
first_series = pd.Series(list("abcdef"))
print(first_series)
# series from ndarray
np_country = np.array(["Nigeria", "Luxembourg", "Japan", "Switzerland", "United states", "Qatar", "Iceland",
                       "Sweden", "Singapore", "Norway"])
s_country = pd.Series(np_country)
print(s_country)
# series from dict
dict_country_gdp = pd.Series([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140],
                             index=["Nigeria", "Luxembourg", "Japan",
                                    "Switzerland", "United states",
                                    "Qatar", "Iceland", "Sweden",
                                    "Singapore", "Norway",
                                    "China", "Malaysia", "India",
                                    "Senegal"])
# series from scalar
print(dict_country_gdp)
scalar_series = pd.Series(5., index=['a', 'b', 'c', 'd', 'e'])
print(scalar_series)
# accessing values in a list
print(dict_country_gdp[0])
print(dict_country_gdp[0:5])
print(dict_country_gdp.loc['Luxembourg'])
print(dict_country_gdp.iloc[0])
# vectorized operations
first_vector_series = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
second_vector_series = pd.Series([5, 6, 7, 8], index=['a', 'b', 'c', 'd'])
print(first_vector_series + second_vector_series)
third_vector_series = pd.Series([4, 5, 6, 7], index=['b', 'c', 'd', 'a'])
print(first_vector_series + third_vector_series)

# Dataframe
# making dataframe from dictionaries
import pandas as pd

olympic_data_list = {'Hostcity': ['London', 'Beijing', 'Athens', 'Sydney', 'Atlanta'], 'Year':
    [2012, 2008, 2004, 2000, 1996], 'No. of participating countries': [205, 204, 201, 200, 197]}
df_olympic_data = pd.DataFrame(olympic_data_list)
print(df_olympic_data)
olympic_data_dict = {'London': {2012: 205}, 'Beijing': {2008: 204}}
df_olympic_dict = pd.DataFrame(olympic_data_dict)
print(df_olympic_dict)
# view dataframe by referring to the column name
print(df_olympic_data.Hostcity)
print(df_olympic_data.Year)
print(df_olympic_data.describe)
# creating df from series
olympic_series_participation = pd.Series([205, 204, 201, 200, 197], index=[2012, 2000, 2004, 2000, 1996])
olympic_series_country = pd.Series(['London', 'Beijing', 'Athens', 'Sydney', 'Atlanta'],
                                   index=[2012, 2000, 2004, 2000, 1996])
df_olympic_series = pd.DataFrame({'No of participating countries': olympic_series_participation,
                                  'Host cities': olympic_series_country})
print(df_olympic_series)

# create data frame from ndarray
import numpy as np

np_array = np.array([2012, 2008, 2004, 2006])
dict_ndarray = {'year': np_array}
df_ndarray = pd.DataFrame(dict_ndarray)
print(df_ndarray)
df_from_df = pd.DataFrame(df_olympic_series)
print(df_from_df)

most_gold_winners = ['United States (46 gold,28 silver, 29 bronze)',
                    'United States (36 gold, 38 silver, 36 bronze)',
                    'United States (36 gold, 39 silver, 29 bronze)',
                    'United States (37 gold, 24 silver, 33 bronze)',
                    'United States (44 gold, 32 silver, 25 bronze)']
df_olympic_data = df_olympic_data.assign(most_medals=most_gold_winners)
print(df_olympic_data)
df_olympic_data = df_olympic_data.assign(no_of_countries_2x= lambda x: x['No. of participating countries'] * 2)
print(df_olympic_data)
print(df_olympic_data.columns)