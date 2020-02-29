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

def freq_table(data_set, index):
    frequency_table = {}
    for app in data_set:
        data_point = app[index]
        if data_point in frequency_table:
            frequency_table[data_point] += 1
        else:
            frequency_table[data_point] = 1
    for key in frequency_table:
        frequency_table[key] = (frequency_table[key]/len(data_set))*100
    
    return frequency_table

def display_table(dataset, index):
    table = freq_table(dataset, index)
    table_display = []
    for key in table:
        key_val_as_tuple = (table[key], key)
        table_display.append(key_val_as_tuple)

    table_sorted = sorted(table_display, reverse = True)
    for entry in table_sorted:
        print(entry[1], ':', entry[0])

# Initial Exploration of Data

apple_header = explore_data(apps_data_apple,0,1) # Header row (column names) in the AppleStore.csv
explore_data(apps_data_apple,1,6,True) # First 5 data rows in AppleStore.csv

google_header = explore_data(apps_data_google,0,1) # Header row (column names) in the googleplaystore.csv
explore_data(apps_data_google,1,6,True) # First 5 data rows in googleplaystore.csv

# Data Cleaning
     # Cleaning Goal 1: googleplaystore.csv has an error for row 10473 (counting header) 

        # Column 'Category' (which should be [1]) was excluded
        # ['Life Made WI-Fi Touchscreen Photo Frame', '1.9', '19', '3.0M', '1,000+', 'Free', '0', 'Everyone', '', 'February 11, 2018', '1.0.19', '4.0 and up']
        
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
        apple_clean_free = []

        for app in google_clean_english:
            if app[6] == 'Free':
                google_clean_english_free.append(app)

        for app in apps_data_apple:
            if app[4] == '0.0':
                apple_clean_free.append(app)

# Frequency Tables

    # Highest Rated
        # Our conclusion was that we'll need to build a frequency table for the prime_genre column of the App Store data set, and for the Genres and Category columns of the Google Play data set.
        # We'll build two functions we can use to analyze the frequency tables:

            # - One function to generate frequency tables that show percentages - function: freq_table
            # - Another function we can use to display the percentages in a descending order - funtion: display_table

        print('Google Play Store - Category Frequency Table',display_table(google_clean_english_free,1))
        print('\n')
        print('Google Play Store - Genre Frequency Table',display_table(google_clean_english_free,9))
        print('\n')
        print('Apple App Store - prime_genre Frequency Table', display_table(apple_clean_free, 11))

        # The frequency tables we analyzed showed us that the App Store is dominated by apps designed for fun, while Google Play shows a more balanced landscape of both practical and fun apps. 
            # Apple App Store - prime_genre Frequency Table Example
                # { Games : 55.64595660749507, Entertainment : 8.234714003944774, Photo & Video : 4.117357001972387, Social Networking : 3.5256410256410255, Education : 3.2544378698224854 }

            # Google Play Store - Category Frequency Table Example
                # { FAMILY : 18.898792733837304, GAME : 9.725826469592688, TOOLS : 8.462146000225657, BUSINESS : 4.592124562789123, LIFESTYLE : 3.9038700214374367 }
        

    