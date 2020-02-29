# Opening CSV Files
opened_file_apple = open('/data_sets/AppleStore.csv')
from csv import reader 
read_file_apple = reader(opened_file_apple) 
apps_data_apple = list(read_file_apple)

opened_file_google = open('/data_sets/googleplaystore.csv')
from csv import reader 
read_file_google = reader(opened_file_google) 
apps_data_google = list(read_file_google)

# Funtions
def explore_data(dataset, start, end, rows_and_columns=False):
    dataset_slice = dataset[start:end]    
    for row in dataset_slice:
        print(row)
        print('\n') 

    if rows_and_columns:
        print('Number of rows:', len(dataset))
        print('Number of columns:', len(dataset[0]))

# Initial Exploration of Data

apple_header = explore_data(apps_data_apple,0,1) # Header row (column names) in the AppleStore.csv
explore_data(apps_data_apple,1,6,True) # First 5 data rows in AppleStore.csv

google_header = explore_data(apps_data_google,0,1) # Header row (column names) in the googleplaystore.csv
explore_data(apps_data_google,1,6,True) # First 5 data rows in googleplaystore.csv

# Data Cleaning
     # Cleaning Goal 1: removing any data for non-English and priced apps)
     # Cleaning Goal 2: googleplaystore.csv has an error for row 10473 (counting header) 
        del apps_data_google[10473]


