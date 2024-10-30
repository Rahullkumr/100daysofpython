# Importing the pandas library, commonly used for data manipulation and analysis
import pandas as pd

# Reading the CSV file into a DataFrame
data = pd.read_csv('./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')


'''
# ============== This is my way ===========================

pfc = data['Primary Fur Color']
fur_color_dict = {
    "Fur Color": ['Gray', 'Cinnamon', 'Black'],
    "Count": []
}
g_count, b_count, c_count = 0, 0, 0
for i in pfc:
    if i in ('Gray', 'Cinnamon', 'Black'):
        g_count += 1 if i == "Gray" else 0
        c_count += 1 if i == "Cinnamon" else 0
        b_count += 1 if i == "Black" else 0
fur_color_dict["Count"] = [g_count, c_count, b_count]
print(fur_color_dict)
'''

# Better way
pfc = data['Primary Fur Color']
grey_squirrel_count = len(data[data['Primary Fur Color'] == 'Gray'])
cinnamon_squirrel_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_squirrel_count = len(data[data['Primary Fur Color'] == 'Black'])

fur_color_dict = {
    "Fur Color": ['Gray', 'Cinnamon', 'Black'],
    "Count": [grey_squirrel_count, cinnamon_squirrel_count, black_squirrel_count]
}

# Creating and printing the DataFrame
df = pd.DataFrame(fur_color_dict)
print(df)

# Saving the DataFrame as a new CSV file with squirrel fur color counts
df.to_csv('./squirrel_count.csv')
