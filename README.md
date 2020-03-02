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