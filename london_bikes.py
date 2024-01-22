# %%
# Uncomment the pip install code below if haven't installed these libraries yet
#!pip install pandas
#!pip install zipfile
#!pip install kaggle

# import the pandas library
import pandas as pd

# import zipfile library (use to extract the file downloaded from Kaggle)
import zipfile

# import kaggle library (use to download the file from Kaggle)
import kaggle


# %%
# read in the csv file as a pandas dataframe
bikes = pd.read_csv('london_merged.csv')

# explore the data
bikes.info()

# %%
bikes.shape

# %%
bikes

# %%
# count the unique values in the weather_code_column
bikes.weather_code.value_counts()

# %%
# count the unique values in the season column
bikes.season.value_counts()

# %%
# specifying the column names that I want to use
new_cols_dict = {
    'timestamp' : 'time',
    'cnt' : 'count',
    't1' : 'temp_real_C',
    't2' : 'temp_feels_like_C',
    'hum' : 'humidity_percent',
    'wind_speed' : 'wind_speed_kph',
    'weather_code' : 'weather',
    'is_holiday' : 'is_holiday',
    'is_weekend' : 'is_weekend',
    'season' : 'season',
}

# renaming the columns to the specified column names
bikes.rename(new_cols_dict, axis=1, inplace=True)

# %%
# changing the humidty values to percentage (i.e. a value between 0 and 1)
bikes.humidity_percent = bikes.humidity_percent/100

# %%
# creating a season dictionary so that we can map the integers 0-3 to the actual written values
season_dict = {
    '0.0': 'spring',
    '1.0': 'summer',
    '2.0': 'fall',
    '3.0': 'winter'
}

# creating a weather dictionary so that we can map the integers to the actual written values
weather_dict = {
    '1.0': 'clear',
    '2.0': 'Scattered clouds',
    '3.0': 'Broken clouds',
    '4.0': 'Cloudy',
    '7.0': 'Rain',
    '10.0': 'Rain with thunderstorm',
    '26.0': 'Snowfall'
}

# changing the seasons column data type to string
bikes.season = bikes.season.astype('str')
# mapping the values 0-3 to the actual written seasons
bikes.season = bikes.season.map(season_dict)

# changing the weather column data type to string
bikes.weather = bikes.weather.astype('str')
# mapping the values to the actual written weathers
bikes.weather = bikes.weather.map(weather_dict)


# %%
# checking the dataframe to see if the mappings worked
bikes.head()

# %%
# writing the final dataframe to an excel file that I will use in Tableau Visualization
bikes.to_excel('london_bikes_final.xlsx', sheet_name='Data')


