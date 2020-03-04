# Profitable App Profiles for the App Store and Google Play Markets

**Premise:**
 For this project, we'll pretend we're working as data analysts for a company that builds Android and iOS mobile apps. We make our apps available on Google Play and the App Store.

 We only build apps that are free to download and install, and our main source of revenue consists of in-app ads. This means our revenue for any given app is mostly influenced by the number of users who use our app — the more users that see and engage with the ads, the better. 

**Goal:**
 Our goal for this project is to analyze data to help our developers understand what type of apps are likely to attract more users. 
 
 To minimize risks and overhead, our validation strategy for an app idea is comprised of three steps:

    * Build a minimal Android version of the app, and add it to Google Play.
    * If the app has a good response from users, we develop it further.
    * If the app is profitable after six months, we build an iOS version of the app and add it to the  App Store.

 Because our end goal is to add the app on both Google Play and the App Store, we need to find app profiles that are successful on both markets. 

**Language:**
 Python

**Tools:**
 Original run in Jupyter Notebook

**Data Sets:**
 * A data set containing data about approximately 10,000 Android apps from Google Play; the data was collected in August 2018.      
    * File: *googleplaystore.csv*
 * A data set containing data about approximately 7,000 iOS apps from the App Store; the data was collected in July 2017.        
    * File: *AppleStore.csv*

---
## Functions

**explore_data()** - Built to explore rows in a more readable way. There is an option in our function to show the number of rows and columns for any data set.

```
def explore_data(dataset, start, end, rows_and_columns=False):
    dataset_slice = dataset[start:end]    
    for row in dataset_slice:
        print(row)
        print('\n') # adds a new (empty) line between rows
        
    if rows_and_columns:
        print('Number of rows:', len(dataset))
        print('Number of columns:', len(dataset[0]))

```
**is_app_English()** - We are not interested in analyzing non-English apps. Some of the apps have non-English names/titles. Our assumption is that a non-English names indicates a non-English app. This function is built to loop through the app names and find at least 3 characters with ASCII values over 127.

```
def is_app_English(string):
    ascii_greater_127 = []
    for character in string:
        value = ord(character)
        if value > 127:
            ascii_greater_127.append(character)
    if len(ascii_greater_127) > 3:
        return False
    else: 
        return True
```
**freq_table() & display_table()** - Two functions used to analyze the frequency tables:

* One function to generate frequency tables that show percentages
* Another function that we can use to display the percentages in a descending order

```
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
```
---
## Opening CSV Files

```
from csv import reader 

### Apple App Store Dataset ###
opened_file_apple = open('/data_sets/AppleStore.csv')
read_file_apple = reader(opened_file_apple) 
apps_data_apple = list(read_file_apple)

### Google Play Store Dataset ###
opened_file_google = open('/data_sets/googleplaystore.csv')
read_file_google = reader(opened_file_google) 
apps_data_google = list(read_file_google)`
```
**Initial Exploration of Data**

```
apple_header = explore_data(apps_data_apple,0,1) # Header row (column names) in the AppleStore.csv

['id', 'track_name', 'size_bytes', 'currency', 'price', 'rating_count_tot', 'rating_count_ver', 'user_rating', 'user_rating_ver', 'ver', 'cont_rating', 'prime_genre', 'sup_devices.num', 'ipadSc_urls.num', 'lang.num', 'vpp_lic']
```
```
explore_data(apps_data_apple,1,6,True) # First 5 data rows in AppleStore.csv

['284882215', 'Facebook', '389879808', 'USD', '0.0', '2974676', '212', '3.5', '3.5', '95.0', '4+', 'Social Networking', '37', '1', '29', '1']


['389801252', 'Instagram', '113954816', 'USD', '0.0', '2161558', '1289', '4.5', '4.0', '10.23', '12+', 'Photo & Video', '37', '0', '29', '1']


['529479190', 'Clash of Clans', '116476928', 'USD', '0.0', '2130805', '579', '4.5', '4.5', '9.24.12', '9+', 'Games', '38', '5', '18', '1']


['420009108', 'Temple Run', '65921024', 'USD', '0.0', '1724546', '3842', '4.5', '4.0', '1.6.2', '9+', 'Games', '40', '5', '1', '1']


['284035177', 'Pandora - Music & Radio', '130242560', 'USD', '0.0', '1126879', '3594', '4.0', '4.5', '8.4.1', '12+', 'Music', '37', '4', '1', '1']


Number of rows: 7198
Number of columns: 16
```
```
google_header = explore_data(apps_data_google,0,1) # Header row (column names) in the googleplaystore.csv

['App', 'Category', 'Rating', 'Reviews', 'Size', 'Installs', 'Type', 'Price', 'Content Rating', 'Genres', 'Last Updated', 'Current Ver', 'Android Ver']
```
```
explore_data(apps_data_google,1,6,True) # First 5 data rows in googleplaystore.csv

['Photo Editor & Candy Camera & Grid & ScrapBook', 'ART_AND_DESIGN', '4.1', '159', '19M', '10,000+', 'Free', '0', 'Everyone', 'Art & Design', 'January 7, 2018', '1.0.0', '4.0.3 and up']


['Coloring book moana', 'ART_AND_DESIGN', '3.9', '967', '14M', '500,000+', 'Free', '0', 'Everyone', 'Art & Design;Pretend Play', 'January 15, 2018', '2.0.0', '4.0.3 and up']


['U Launcher Lite – FREE Live Cool Themes, Hide Apps', 'ART_AND_DESIGN', '4.7', '87510', '8.7M', '5,000,000+', 'Free', '0', 'Everyone', 'Art & Design', 'August 1, 2018', '1.2.4', '4.0.3 and up']


['Sketch - Draw & Paint', 'ART_AND_DESIGN', '4.5', '215644', '25M', '50,000,000+', 'Free', '0', 'Teen', 'Art & Design', 'June 8, 2018', 'Varies with device', '4.2 and up']


['Pixel Draw - Number Art Coloring Book', 'ART_AND_DESIGN', '4.3', '967', '2.8M', '100,000+', 'Free', '0', 'Everyone', 'Art & Design;Creativity', 'June 20, 2018', '1.1', '4.4 and up']


Number of rows: 10842
Number of columns: 13

```
---
## Data Cleaning

### Cleaning Goal 1: Incorrect Entry
The googleplaystore.csv has an error in row 10473 (counting header) 

```
print(google_apps_Data[10473])  # incorrect row
print('\n')
print(google_header)  # header
```
```
['Life Made WI-Fi Touchscreen Photo Frame', '1.9', '19', '3.0M', '1,000+', 'Free', '0', 'Everyone', '', 'February 11, 2018', '1.0.19', '4.0 and up']


['App', 'Category', 'Rating', 'Reviews', 'Size', 'Installs', 'Type', 'Price', 'Content Rating', 'Genres', 'Last Updated', 'Current Ver', 'Android Ver']

```
The data for column 'Category' (which should be index 1 ([1])) was excluded
We will remove the row.

`del apps_data_google[10473]`

### Cleaning Goal 2: Duplicates
The googleplaystore.csv has multiple entries for some apps. 

First we must figure out which apps have multiple entries.

```
        duplicate_apps = []
        unique_apps = []

        for app in apps_data_google:
            name = app[0]
            if name in unique_apps:
                duplicate_apps.append(name)
            else: 
                unique_apps.append(name)
```
```
print('Number of duplicate apps:', len(duplicate_apps))
print('\n')
print('Examples of duplicate apps:', duplicate_apps[:15])

Number of duplicate apps: 1181


Examples of duplicate apps: ['Quick PDF Scanner + OCR FREE', 'Box', 'Google My Business', 'ZOOM Cloud Meetings', 'join.me - Simple Meetings', 'Box', 'Zenefits', 'Google Ads', 'Google My Business', 'Slack', 'FreshBooks Classic', 'Insightly CRM', 'QuickBooks Accounting: Invoicing & Expenses', 'HipChat - Chat Built for Teams', 'Xero Accounting Software']
```

We do not want to remove the duplicate entries at random. If we look at the multiple entries for the instagram app, we can see that the entries have different 'user ratings' count.

```
for app in google_apps_data:
    name = app[0]
    if name == 'Instagram':
        print(app)
```
```
['Instagram', 'SOCIAL', '4.5', '66577313', 'Varies with device', '1,000,000,000+', 'Free', '0', 'Teen', 'Social', 'July 31, 2018', 'Varies with device', 'Varies with device']
['Instagram', 'SOCIAL', '4.5', '66577446', 'Varies with device', '1,000,000,000+', 'Free', '0', 'Teen', 'Social', 'July 31, 2018', 'Varies with device', 'Varies with device']
['Instagram', 'SOCIAL', '4.5', '66577313', 'Varies with device', '1,000,000,000+', 'Free', '0', 'Teen', 'Social', 'July 31, 2018', 'Varies with device', 'Varies with device']
['Instagram', 'SOCIAL', '4.5', '66509917', 'Varies with device', '1,000,000,000+', 'Free', '0', 'Teen', 'Social', 'July 31, 2018', 'Varies with device', 'Varies with device']
```
We have decided to find and use the entry with the highest user rating count, per duplicate app.

```
        reviews_max = {}

        for app in apps_data_google[1:]:
            name = app[0]
            n_reviews = float(app[3])
            
            if name in reviews_max and reviews_max[name] < n_reviews:
                reviews_max[name] = n_reviews
            elif name not in reviews_max: 
                reviews_max[name] = n_reviews
```

We will remove any duplicate that has a user rating count that is lower than the count listed in the dictionary above 

```
google_clean = []
already_added = []

for app in apps_data_google[1:]:
    name = app[0]
    n_reviews = float(app[3])
            
    if (reviews_max[name] == n_reviews) and (name not in already_added):
        google_clean.append(app)
        already_added.append(name)
```
### Cleaning Goal 3: Non-English Apps

We have come across apps that have non-English names. Our assumption is that a non-English name is an indication that the app is an non-English app. We do not want to analyze non-English apps. The characters we commonly use in English generally have ASCII (American Standard Code for Information Interchange) values in the of range 0 to 127. If we loop through the characters in the app names, and search for characters with an ASCII greater than 127, we can guess whether or not an app is an English based app. 

If an app name has more than 3 characters with ASCII values over 127, we will exclude the app data. This logic is our best effort to avoid removing apps that may have English names, but symbols like emoticons. 

```
        google_clean_english = []
        apple_clean_english = []

        for app in google_clean:
            if is_app_English(app[0]):
                google_clean_english.append(app)
        
        for app in apps_data_apple:
            if is_app_English(app[1]):
                apple_clean_english.append(app)
```
```
print(is_app_English('Docs To Go™ Free Office Suite'))
print(is_app_English('Instachat 😜'))
print(is_app_English('爱奇艺PPS -《欢乐颂2》电视剧热播'))

True
True
False
```

### Cleaning Goal 4: Removing Non-Free Apps

We only want to analyze the data for free apps, and thus must removed any priced apps from out dataset.

```
google_final = []
apple_final = []

for app in google_clean_english:
    if app[7] == 'Free':
        google_final.append(app)

for app in apple_clean_english:
    if app[4] == '0.0':
        apple_final.append(app)
```
---
## Analysis

### Most Common Genre

To minimize risks and overhead, our validation strategy for an app idea is comprised of three steps:

* Build a minimal Android version of the app, and add it to Google Play.
* If the app has a good response from users, we then develop it further.
* If the app is profitable after six months, we also build an iOS version of the app and add it to the App Store.

Our goal is to find app profiles that are successful on both markets. We will begin our analysis by building a frequency table for the prime_genre column of the App Store data set, and the Genres and Category columns of the Google Play data set. 

We will use the freq_table() and display_table() functions. 
* freq_tables() - will generate frequency tables that show percentages
* display_table - will display the percentages in a descending order

```
print('Google - Category Frequency Table',display_table(google_final,1))

FAMILY : 18.898792733837304
GAME : 9.725826469592688
TOOLS : 8.462146000225657
BUSINESS : 4.592124562789123
LIFESTYLE : 3.9038700214374367
PRODUCTIVITY : 3.8925871601038025
```
```
print('Apple - prime_genre Frequency Table', display_table(apple_final, 11))

Games : 55.64595660749507
Entertainment : 8.234714003944774
Photo & Video : 4.117357001972387
Social Networking : 3.5256410256410255
Education : 3.2544378698224854

```
In the Apple App Store, among the free English apps, more than a half (55%) are games. Entertainment apps are close to 8%.

At first glance games only make up 9% of apps, and it seems close to 19% of the apps are designed for family use. However, if we investigate this further, we can see that the family category means mostly games for kids.

We must investigate further to determine if the numerous game apps, translate into numerous customers. 

### Most Installs
```
p_genres = freq_table(apple_clean_free, 11)

{'Utilities': 2.687376725838264, 'News': 1.4299802761341223, 'Food & Drink': 1.0601577909270217, 'Reference': 0.4930966469428008, 'Book': 1.6272189349112427, 'Shopping': 2.983234714003945, 'Productivity': 1.5285996055226825, 'Business': 0.4930966469428008, 'Sports': 1.947731755424063, 'Navigation': 0.4930966469428008, 'Games': 55.64595660749507, 'Health & Fitness': 1.8737672583826428, 'Education': 3.2544378698224854, 'Catalogs': 0.22189349112426035, 'Photo & Video': 4.117357001972387, 'Lifestyle': 2.3175542406311638, 'Entertainment': 8.234714003944774, 'Weather': 0.7642998027613412, 'Social Networking': 3.5256410256410255, 'Music': 1.6518737672583828, 'Finance': 2.0710059171597637, 'Travel': 1.3806706114398422, 'Medical': 0.19723865877712032}

```






