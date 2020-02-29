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

def app_English(string):
    ascii_greater_127 = []
    for character in string:
        value = ord(character)
        if value > 127:
            ascii_greater_127.append(character)
    if len(ascii_greater_127) > 3:
        return False
    else: 
        return True

# Initial Exploration of Data

apple_header = explore_data(apps_data_apple,0,1) # Header row (column names) in the AppleStore.csv
explore_data(apps_data_apple,1,6,True) # First 5 data rows in AppleStore.csv

google_header = explore_data(apps_data_google,0,1) # Header row (column names) in the googleplaystore.csv
explore_data(apps_data_google,1,6,True) # First 5 data rows in googleplaystore.csv

# Data Cleaning
     # Cleaning Goal 1: googleplaystore.csv has an error for row 10473 (counting header) 

        # Column 'Category' (which should be [1]) was excluded
        ['Life Made WI-Fi Touchscreen Photo Frame', '1.9', '19', '3.0M', '1,000+', 'Free', '0', 'Everyone', '', 'February 11, 2018', '1.0.19', '4.0 and up']
        
        del apps_data_google[10473]

     # Cleaning Goal 2: googleplaystore.csv has duplicate entries for apps
        duplicate_apps = []
        unique_apps = []

        for app in apps_data_google:
            name = app[0]
            if name in unique_apps:
                duplicate_apps.append(name)
            else: 
                unique_apps.append(name)

        print('Number of duplicate apps:', len(duplicate_apps))
        print('\n')
        print('Examples of duplicate apps:', duplicate_apps[:15])

        # Number of duplicate apps: 1181
        # Examples of duplicate apps: ['Quick PDF Scanner + OCR FREE', 'Box', 'Google My Business', 'ZOOM Cloud Meetings', 'join.me - Simple Meetings', 'Box', 'Zenefits', 'Google Ads', 'Google My Business', 'Slack', 'FreshBooks Classic', 'Insightly CRM', 'QuickBooks Accounting: Invoicing & Expenses', 'HipChat - Chat Built for Teams', 'Xero Accounting Software']
       
        # We will find the data entry with the highest 'Rating'
        reviews_max = {}

        for app in apps_data_google[1:]:
            name = app[0]
            n_reviews = float(app[3])
            
            if name in reviews_max and reviews_max[name] < n_reviews:
                reviews_max[name] = n_reviews
            if name not in reviews_max: 
                reviews_max[name] = n_reviews
        
        # We will remove any data with a lower rating than the rating in the above dictionary
        google_clean = []
        already_added = []

        for app in apps_data_google[1:]:
            name = app[0]
            n_reviews = float(app[3])
            
            if reviews_max[name] == n_reviews and name not in already_added:
                google_clean.append(app)
                already_added.append(name)

     # Cleaning Goal 3: removing any data for non-English
        # Assumption: 
            # Characters we commonly use in an English text are all in the range 0 to 127, according to the ASCII (American Standard Code for Information Interchange) system. 
            # If we loop through the characters in the app name to search for characters with an ASCII greater than 127, we can guess whether or not an app is an English based app. If an app name has more than 3 characters with ASCII values over 127, we will exclude the app data.

        google_clean_english = []
        for app in google_clean:
            if app_English(app[0]) == True:
                google_clean_english.append(app)
    
    # Cleaning Goal 4: removing any data for non-free/priced apps
    google_clean_english_free = []

    for app in google_clean_english:
        if app[6] == 'Free':
            google_clean_english_free.append(app)

