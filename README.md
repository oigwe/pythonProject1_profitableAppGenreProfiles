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
**Opening CSV Files**

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
**Functions**

explore_data() - to explore rows in a more readable way. There is an option in our function to show the number of rows and columns for any data set.

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
`explore_data(apps_data_apple,1,6,True)`

['284882215', 'Facebook', '389879808', 'USD', '0.0', '2974676', '212', '3.5', '3.5', '95.0', '4+', 'Social Networking', '37', '1', '29', '1']


['389801252', 'Instagram', '113954816', 'USD', '0.0', '2161558', '1289', '4.5', '4.0', '10.23', '12+', 'Photo & Video', '37', '0', '29', '1']


['529479190', 'Clash of Clans', '116476928', 'USD', '0.0', '2130805', '579', '4.5', '4.5', '9.24.12', '9+', 'Games', '38', '5', '18', '1']


['420009108', 'Temple Run', '65921024', 'USD', '0.0', '1724546', '3842', '4.5', '4.0', '1.6.2', '9+', 'Games', '40', '5', '1', '1']


['284035177', 'Pandora - Music & Radio', '130242560', 'USD', '0.0', '1126879', '3594', '4.0', '4.5', '8.4.1', '12+', 'Music', '37', '4', '1', '1']


Number of rows: 7198
Number of columns: 16
