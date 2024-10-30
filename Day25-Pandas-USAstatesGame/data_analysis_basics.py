""" BASICS OF DATA ANALYSIS """


# with open('./weather_data.csv', 'r') as file:
#     data = file.readlines()
#     print(data)
"""There is a lot of headache in cleaning the above data, so try other way (see below)"""


# import csv
# with open('./weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#
#     print(temperatures)
"""
A lot of lines of code is written just to get one column, what if there are 100s of columns and complex data,
so it is not a convenient way. Now let's use PANDAS library and see the magic.
"""


import pandas as pd
data = pd.read_csv('./weather_data.csv')
print(data['temp'])

# DataFrame:    whole table of Excel sheet or google sheet (2D)
                # eg: data
# Series:       a column of Excel sheet or google sheet (1D)
                # eg: data['temp']

data_as_dict = data.to_dict()
temp_list = data['temp'].to_list()
print(data_as_dict)
print(temp_list)


print('Average Temperature: ', sum(temp_list)/len(temp_list))
print('Average temp using series: ', data['temp'].mean())
print('Max temp using series: ', data['temp'].max())        # data['temp']  ==  data.temp
print('Max temp using series: ', data.temp.max())
print(data.condition)


# Get data in row
print(data[data.day == 'Monday'])               # its dataframe

# Get the row which has maximum temperature
print(data[data.temp == data.temp.max()])       # its dataframe

# Get Monday's condition
print(data[data.day == "Monday"].condition)

# challenge: show Monday's temperature in Fahrenheit ((0°C × 9/5) + 32 = 32°F)
monday_temp = data.temp[0]
print(monday_temp)
print("Monday's temp in Fahrenheit: ", monday_temp * 9/5 + 32, "°F")


# create a DataFrame from scratch
data_dict = {
    "names": ['Amit', 'Rohit', 'Sumit'],
    "score": [45, 73, 66]
}
df_from_scratch = pd.DataFrame(data_dict)
print(df_from_scratch)


# save the DataFrame in csv format
df_from_scratch.to_csv('./students_data.csv')       # path where you want to save
