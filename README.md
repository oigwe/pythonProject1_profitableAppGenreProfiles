# PROFITABLE APP PROFILES 
### FOR THE APP STORE AND GOOGLE PLAY MARKETS


[Introduction](#PROFITABLE-APP-PROFILES ) | [Method: Primary Functions](#PRIMARY-FUNCTIONS-OF-USE) | [Method: Initial Exploration of Data](#INITIAL-EXPLORATION-OF-DATA) | [Method: Data Cleaning](#CLEANING-THE-DATA) | [Analysis](#ANALYSIS) | [ Conclusion](#CONCLUSION)


**Premise**
For this project, we are pretending that we work as data analysts for a company that builds Android and iOS mobile apps. 

The company only builds apps that are free to download and install, and the main source of revenue consists of in-app ads. This means that the revenue for any given app is highly influenced by the number of users who use our app. Thus the more users that engage with the ads, the better for the companies revenue. 

**Goal**
Our goal for this project is to analyze data to help the developer team understand what type of app is likely to attract the most users. 

**Language**
Python

**Tools**
Originally run in Jupyter Notebook

**Data Sets**
* A data set containing data about approximately 10,000 Android apps from Google Play; the data was collected in August 2018.      
    * File: *googleplaystore.csv*
* A data set containing data about approximately 7,000 iOS apps from the App Store; the data was collected in July 2017.        
    * File: *AppleStore.csv*

***Conclusion***

The books and reference genre is a fairly popular genre. We found this genre has the potential to work well in both the App Store and Google Play stores, as our aim is to recommend an app genre that shows potential for being profitable in both stores. [Please read for more detail](#CONCLUSION)

---
---

# METHOD OF ANALYSIS

## PRIMARY FUNCTIONS OF USE

### Function for data exploration

This function is used to print rows in a readable way.


```python
def explore_data(dataset, start, end, rows_and_columns=False):
    dataset_slice = dataset[start:end]    
    for row in dataset_slice:
        print(row)


    if rows_and_columns:
        print('Number of rows:', len(dataset))
        print('Number of columns:', len(dataset[0]))
```

The function has 4 inputs:
<ul>
<li> dataset : which is expected to be a list of lists.</li>
<li> start and end:  which are both expected to be integers and represent the starting and the ending indices of a slice from the data set.</li>
<li> rows_and_columns: which is expected to be a Boolean. This parameter will determine if the function prints the number of rows and columns in the data set</li>
</ul>

***Use***


```python
explore_data(apps_data_apple,0,1)      #header for applestore data set
```

    ['id', 'track_name', 'size_bytes', 'currency', 'price', 'rating_count_tot', 'rating_count_ver', 'user_rating', 'user_rating_ver', 'ver', 'cont_rating', 'prime_genre', 'sup_devices.num', 'ipadSc_urls.num', 'lang.num', 'vpp_lic']



```python
explore_data(apps_data_apple,1,3,True) #partial table body for applestore data
```

    ['284882215', 'Facebook', '389879808', 'USD', '0.0', '2974676', '212', '3.5', '3.5', '95.0', '4+', 'Social Networking', '37', '1', '29', '1']
    ['389801252', 'Instagram', '113954816', 'USD', '0.0', '2161558', '1289', '4.5', '4.0', '10.23', '12+', 'Photo & Video', '37', '0', '29', '1']
    Number of rows: 7198
    Number of columns: 16


---
### Function for language determination

We are not interested in analyzing non-English apps. During exploration, we noticed that some of the apps have non-English names/titles. Our assumption is that a non-English name indicates a non-English app. This function is built to loop through app names and find at least 3 characters with ASCII values over 127.


```python
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

print(app_English('Instagram'))
print(app_English('爱奇艺PPS -《欢乐颂2》电视剧热播'))
```

    True
    False


***Use & Output***


```python
google_clean_english_test = []

for app in apps_data_google:
    if app_English(app[0]) == True:
        google_clean_english_test.append(app)

print("Number of English Apps: ", len(google_clean_english_test))

print("Example of Returned App Data:   ", google_clean_english_test[1:3])
```

    Number of English Apps:  10797
    Example of Returned App Data:    [['Photo Editor & Candy Camera & Grid & ScrapBook', 'ART_AND_DESIGN', '4.1', '159', '19M', '10,000+', 'Free', '0', 'Everyone', 'Art & Design', 'January 7, 2018', '1.0.0', '4.0.3 and up'], ['Coloring book moana', 'ART_AND_DESIGN', '3.9', '967', '14M', '500,000+', 'Free', '0', 'Everyone', 'Art & Design;Pretend Play', 'January 15, 2018', '2.0.0', '4.0.3 and up']]


---
### Functions to create frequency and display tables

Two functions were created to faciliate in the data analyzation process:

* One function to generate frequency tables that show percentages
* Another function that we can use to display the percentages in a descending order


```python
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
---

## INITIAL EXPLORATION OF DATA

### Opening the data sets

Importing the reader object from the csv library


```python
from csv import reader 
```

Opening, reading, and creating a list of the values - for both data sets


```python
# The App Store data set 
opened_file_apple = open('AppleStore.csv')
read_file_apple = reader(opened_file_apple) 
apps_data_apple = list(read_file_apple)

# The Google Play data set 
opened_file_google = open('googleplaystore.csv')
read_file_google = reader(opened_file_google) 
apps_data_google = list(read_file_google)
```

---

### Exploring the data
The **Header row** (column names) in the **applestore.csv** can be found below


```python
apple_header = explore_data(apps_data_apple,0,1)
```

    ['id', 'track_name', 'size_bytes', 'currency', 'price', 'rating_count_tot', 'rating_count_ver', 'user_rating', 'user_rating_ver', 'ver', 'cont_rating', 'prime_genre', 'sup_devices.num', 'ipadSc_urls.num', 'lang.num', 'vpp_lic']


A sampling (first 2) of the rows in the AppleStore.csv **table body** can be found below


```python
explore_data(apps_data_apple,1,3,True) 
```

    ['284882215', 'Facebook', '389879808', 'USD', '0.0', '2974676', '212', '3.5', '3.5', '95.0', '4+', 'Social Networking', '37', '1', '29', '1']
    ['389801252', 'Instagram', '113954816', 'USD', '0.0', '2161558', '1289', '4.5', '4.0', '10.23', '12+', 'Photo & Video', '37', '0', '29', '1']
    Number of rows: 7198
    Number of columns: 16


The same display of information can be shown from the data read from the **googleplaystore.csv**

***Header row***


```python
google_header = explore_data(apps_data_google,0,1) 
```

    ['App', 'Category', 'Rating', 'Reviews', 'Size', 'Installs', 'Type', 'Price', 'Content Rating', 'Genres', 'Last Updated', 'Current Ver', 'Android Ver']


***Sample table body***


```python
explore_data(apps_data_google,1,6,True) 
```

    ['Photo Editor & Candy Camera & Grid & ScrapBook', 'ART_AND_DESIGN', '4.1', '159', '19M', '10,000+', 'Free', '0', 'Everyone', 'Art & Design', 'January 7, 2018', '1.0.0', '4.0.3 and up']
    ['Coloring book moana', 'ART_AND_DESIGN', '3.9', '967', '14M', '500,000+', 'Free', '0', 'Everyone', 'Art & Design;Pretend Play', 'January 15, 2018', '2.0.0', '4.0.3 and up']
    ['U Launcher Lite – FREE Live Cool Themes, Hide Apps', 'ART_AND_DESIGN', '4.7', '87510', '8.7M', '5,000,000+', 'Free', '0', 'Everyone', 'Art & Design', 'August 1, 2018', '1.2.4', '4.0.3 and up']
    ['Sketch - Draw & Paint', 'ART_AND_DESIGN', '4.5', '215644', '25M', '50,000,000+', 'Free', '0', 'Teen', 'Art & Design', 'June 8, 2018', 'Varies with device', '4.2 and up']
    ['Pixel Draw - Number Art Coloring Book', 'ART_AND_DESIGN', '4.3', '967', '2.8M', '100,000+', 'Free', '0', 'Everyone', 'Art & Design;Creativity', 'June 20, 2018', '1.1', '4.4 and up']
    Number of rows: 10842
    Number of columns: 13


---
---

## CLEANING THE DATA

### Cleaning Goal 1: googleplaystore.csv has an error for row 10473 (counting header) 

The data for column 'Category' (which should be index 1) was ommitted.

Data with correct data presentation. Note that the category is 'ART_AND_DESIGN':

    ['Pixel Draw - Number Art Coloring Book', 'ART_AND_DESIGN', '4.3', '967', '2.8M', '100,000+', 'Free', '0', 'Everyone', 'Art & Design;Creativity', 'June 20, 2018', '1.1', '4.4 and up']
    
The current incorrect presentation for row 10473

    ['Life Made WI-Fi Touchscreen Photo Frame', '1.9', '19', '3.0M', '1,000+', 'Free', '0', 'Everyone', '', 'February 11, 2018', '1.0.19', '4.0 and up']
    
To correct this anomaly we will delete the row. 


```python
del apps_data_google[10473]
```

---

### Cleaning Goal 2: googleplaystore.csv has duplicate entries for certain apps

During the exploration of the Google Play data set, we noticed that certain apps have duplicate entries. 
For instance, Instagram has four entries:


```python
for app in apps_data_google:
    if app[0] == "Instagram":
        print(app)
```

    ['Instagram', 'SOCIAL', '4.5', '66577313', 'Varies with device', '1,000,000,000+', 'Free', '0', 'Teen', 'Social', 'July 31, 2018', 'Varies with device', 'Varies with device']
    ['Instagram', 'SOCIAL', '4.5', '66577446', 'Varies with device', '1,000,000,000+', 'Free', '0', 'Teen', 'Social', 'July 31, 2018', 'Varies with device', 'Varies with device']
    ['Instagram', 'SOCIAL', '4.5', '66577313', 'Varies with device', '1,000,000,000+', 'Free', '0', 'Teen', 'Social', 'July 31, 2018', 'Varies with device', 'Varies with device']
    ['Instagram', 'SOCIAL', '4.5', '66509917', 'Varies with device', '1,000,000,000+', 'Free', '0', 'Teen', 'Social', 'July 31, 2018', 'Varies with device', 'Varies with device']


In order to gain a stronger understanding on the extent of the duplication, we temporarily filtered the data set for duplicates. In total there were 1181 duplicated apps. 


```python
duplicate_apps = []
unique_apps = []

for app in apps_data_google:
    name = app[0]
    if name in unique_apps:
        duplicate_apps.append(name)
    else: 
        unique_apps.append(name)
```

A sampling of the app titles that were found to be duplicated are:


```python
print(duplicate_apps[:6])
```

    ['Quick PDF Scanner + OCR FREE', 'Box', 'Google My Business', 'ZOOM Cloud Meetings', 'join.me - Simple Meetings', 'Box']


It was noted that although the duplicated entries held very similar data, they were not exact duplications. By reviewing the Instagram duplicates (above) it can be noted that the entries had different 'number of reviews' (index 3). We decided to filter our duplicates by finding and keeping only one entry per app. The entry will be the one with the highest 'number of reviews'. All other duplicates will be removed from consideration.


```python
reviews_max = {}

for app in apps_data_google[1:]:
    name = app[0]               # App Name
    n_reviews = float(app[3])   # Number of reviews for entry as found in the original data set
            
    if name in reviews_max and reviews_max[name] < n_reviews:
        reviews_max[name] = n_reviews
    elif name not in reviews_max: 
        reviews_max[name] = n_reviews

```

To do this, we created a dictionary, where each key is a unique app name and the corresponding value is the highest number of reviews of that app.

We then used the information stored in the dictionary and created a new data set, which will have only one entry per app (the entry with the highest number of reviews).


```python
google_clean = []
already_added = []

for app in apps_data_google[1:]:
    name = app[0]
    n_reviews = float(app[3])
            
    if (reviews_max[name] == n_reviews) and (name not in already_added):
        google_clean.append(app)
        already_added.append(name)
```

---

### Cleaning Goal 3: removing any data for non-English

We are not interested in analyzing non-English apps. During exploration, we noticed that some of the apps have non-English names/titles. We assume that a non-English name indicates a non-English app. Commonly used English characters are all in the ASCII range of 0 to 127 (ASCII: American Standard Code for Information Interchange system). We built the **app_English()** function, found above, to loop through app names and find more than 3 characters with ASCII values over 127. The function will return **False** if an inputted app name meets the state requirements. Otherwise, the function will return **True**. Any apps that return true will be added to a new data set. We believe that the requirements are sensitive enough to remove the majority (if not all) of the non-English apps, while providing enough leeway to ignore app names that may have special characters, such as emoticons. 



```python
google_clean_english = []
apple_clean_english = []

for app in google_clean:
    if app_English(app[0]) == True:
        google_clean_english.append(app)
        
for app in apps_data_apple:
    if app_English(app[1]) == True:
        apple_clean_english.append(app)
```

---

### Cleaning Goal 4: removing any data for non-free/priced apps

As mentioned in the introduction, the company only builds apps that are free to download and install. The main source of revenue is in-app ads. The current data sets contain both free and non-free apps. We will isolate any free apps by placing them in a new data set.


```python
google_final = []
apple_final = []

for app in google_clean_english:
    if app[6] == 'Free':
        google_final.append(app)

for app in apple_clean_english:
    if app[4] == '0.0':
        apple_final.append(app)
```

---
---

## ANALYSIS

### Most Common Genre

To minimize risks and overhead, the developer team's validation strategy for an app idea is comprised of the following three steps:

* Build a minimal Android version of the app, and add it to Google Play.
* If the app has a good response from users, then develop it further.
* If the app is profitable after six months, the company will also build an iOS version of the app and add it to the App Store.

Our goal is to find app profiles that are successful in both markets. We will begin our analysis by building a frequency table for the **prime_genre** column of the App Store data set, and the **Genres** and **Category** columns of the Google Play data set. This analysis will determine which genre has the most applications. 

We will use the **freq_table()** and **display_table()** functions. 
* freq_tables() - will generate frequency tables that show percentages
* display_table() - will display the percentages in a descending order


**Google Play Store - <em>'Category'<em> Frequency Table**
<br>
Based on the data, the most common app category, in the Google Play Store, is the **Family** category (~19%). However, upon further investigation, we observed that the family category is made up of mostly games for kids. 
    
![Family category from Google Play Store](https://camo.githubusercontent.com/9bf24b9efc3d88a3d55f5c09e314987941f0bab5/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f64712d636f6e74656e742f3335302f7079316d385f66616d696c792e706e67)


```python
print(display_table(google_final,1))
```

    FAMILY : 18.898792733837304
    GAME : 9.725826469592688
    TOOLS : 8.462146000225657
    BUSINESS : 4.592124562789123
    LIFESTYLE : 3.9038700214374367
    PRODUCTIVITY : 3.8925871601038025
    FINANCE : 3.7007785174320205
    MEDICAL : 3.5315355974275078
    SPORTS : 3.396141261423897
    PERSONALIZATION : 3.317161232088458
    COMMUNICATION : 3.2381812027530184
    HEALTH_AND_FITNESS : 3.0802211440821394
    PHOTOGRAPHY : 2.944826808078529
    NEWS_AND_MAGAZINES : 2.798149610741284
    SOCIAL : 2.6627552747376737
    TRAVEL_AND_LOCAL : 2.335552296062281
    SHOPPING : 2.245289405393208
    BOOKS_AND_REFERENCE : 2.1437436533904997
    DATING : 1.8616721200496444
    VIDEO_PLAYERS : 1.7939749520478394
    MAPS_AND_NAVIGATION : 1.399074805370642
    FOOD_AND_DRINK : 1.241114746699763
    EDUCATION : 1.1621347173643235
    ENTERTAINMENT : 0.9590432133589079
    LIBRARIES_AND_DEMO : 0.9364774906916393
    AUTO_AND_VEHICLES : 0.9251946293580051
    HOUSE_AND_HOME : 0.8236488773552973
    WEATHER : 0.8010831546880289
    EVENTS : 0.7108202640189552
    PARENTING : 0.6544059573507841
    ART_AND_DESIGN : 0.6431230960171499
    COMICS : 0.6205573733498815
    BEAUTY : 0.5979916506826132
    None


The same process was used to analyze for the App Store data.  

**App Store - <em>'prime_genres'<em> Frequency Table**
<br>
Based on the data, the most common app category, in the App Store, is the **Games** genre.
In the App Store, among the free English apps, more than a half (approx. 58%) are games. Entertainment apps (approx. 8%), followed by photo and video apps (approx. 5%). Only 3.66% of the apps are educational, followed by social networking apps which only account for 3.29% of the apps in the data set.


```python
app_p_genres = display_table(apple_final, 11)
print(app_p_genres)
```

    Games : 58.16263190564867
    Entertainment : 7.883302296710118
    Photo & Video : 4.9658597144630665
    Education : 3.662321539416512
    Social Networking : 3.2898820608317814
    Shopping : 2.60707635009311
    Utilities : 2.5139664804469275
    Sports : 2.1415270018621975
    Music : 2.0484171322160147
    Health & Fitness : 2.0173805090006205
    Productivity : 1.7380509000620732
    Lifestyle : 1.5828677839851024
    News : 1.3345747982619491
    Travel : 1.2414649286157666
    Finance : 1.1173184357541899
    Weather : 0.8690254500310366
    Food & Drink : 0.8069522036002483
    Reference : 0.5586592178770949
    Business : 0.5276225946617008
    Book : 0.4345127250155183
    Navigation : 0.186219739292365
    Medical : 0.186219739292365
    Catalogs : 0.12414649286157665
    None


**Conclusion** Based on initial analysis, **Games** are the most common genre in both the App Store and the Google Play Store. 

---

### Most Installs

We cannot responsibly suggest that our development team build a game app, at this point in the analysis. We have only determined which app type is the most frequently **built**. We do not know if the rate of game downloads is comparable. We must analyze which genre has the most installations.

For the Google Play data set, we can find the information needed in the **Installs** column, but the App Store data set does not have this specific data. We will use the total number of user ratings as a proxy, which we can find in the **rating_count_tot** app. 

**Assumption** - Our assumption is that the number of installations and the number of reviews can be a proxy for user engagement. 
<br>
**Assumption** - There will be only one review per installation

**App Store** We will calculate the average number of user ratings per app genre on the App Store:


```python
p_genre_apple = freq_table(apple_final, 11)

p_genre_apple_sort = []

for genre in p_genre_apple:
    total = 0
    len_genre = 0
    
    for app in apple_final:
        genre_app = app[11]
        
        if genre_app == genre:            
            num_ratings = float(app[5])
            total += num_ratings
            len_genre += 1
    
    avg_num_ratings = int(total / len_genre)
    
    p_genre_apple_sort.append([avg_num_ratings , genre])

sorted(p_genre_apple_sort, reverse = True)
```




    [[86090, 'Navigation'],
     [74942, 'Reference'],
     [71548, 'Social Networking'],
     [57326, 'Music'],
     [52279, 'Weather'],
     [39758, 'Book'],
     [33333, 'Food & Drink'],
     [31467, 'Finance'],
     [28441, 'Photo & Video'],
     [28243, 'Travel'],
     [26919, 'Shopping'],
     [23298, 'Health & Fitness'],
     [23008, 'Sports'],
     [22788, 'Games'],
     [21248, 'News'],
     [21028, 'Productivity'],
     [18684, 'Utilities'],
     [16485, 'Lifestyle'],
     [14029, 'Entertainment'],
     [7491, 'Business'],
     [7003, 'Education'],
     [4004, 'Catalogs'],
     [612, 'Medical']]



The top five genres that have the highest number of average user ratings are:

**Navigation** - 86,090 ratings/installs <br>
**Reference** - 74,942 ratings/installs <br>
**Social Networking** - 71,548 ratings/installs <br>
**Music** - 57,326 ratings/installs <br>
**Weather** - 52,279 ratings/installs <br>

**Google Play Store** We will calculate the average number of installs per app category on the Google Play Store:


```python
display_table(google_final, 5)
```

    1,000,000+ : 15.728308699086089
    100,000+ : 11.55365000564143
    10,000,000+ : 10.549475346947986
    10,000+ : 10.199706645605326
    1,000+ : 8.394448832223853
    100+ : 6.916393997517771
    5,000,000+ : 6.826131106848697
    500,000+ : 5.562450637481666
    50,000+ : 4.772650344127271
    5,000+ : 4.513144533453684
    10+ : 3.542818458761142
    500+ : 3.2494640640866526
    50,000,000+ : 2.3017037120613786
    100,000,000+ : 2.1324607920568655
    50+ : 1.9180864267178157
    5+ : 0.7898002933543946
    1+ : 0.5077287600135394
    500,000,000+ : 0.270788672007221
    1,000,000,000+ : 0.2256572266726842
    0+ : 0.045131445334536835


At first glance, the imprecision of the data may seem like it would be a problem. But we do not believe that this is the case. Our goal is to get a general idea of which app category performs the best. We will leave the numbers as they are - we will consider that an app with 100,000+ installs has 100,000 installs, and an app with 1,000,000+ installs has 1,000,000 installs, and so on. 


The installation figures are presented in the csv as a strings. We will convert the strings into floats. 


```python
categories = freq_table(google_final, 1)
categories_sort = []

for category in categories:
    total = 0
    len_category = 0
    
    for app in google_final:
        category_app = app[1]
        
        if category_app == category:
            remove = ''
            if '+' in app[5]:
                remove = app[5].translate({ord('+'): None})
            if ',' in app[5]:
                remove = remove.translate({ord(','): None})
            installs = float(remove)
            total += installs
            len_category += 1
            
    avg_installs = total/len_category
    
    categories_sort.append([avg_installs , category])

sorted(categories_sort, reverse = True)
```




    [[38456119.167247385, 'COMMUNICATION'],
     [24727872.452830188, 'VIDEO_PLAYERS'],
     [23253652.127118643, 'SOCIAL'],
     [17840110.40229885, 'PHOTOGRAPHY'],
     [16787331.344927534, 'PRODUCTIVITY'],
     [15588015.603248259, 'GAME'],
     [13984077.710144928, 'TRAVEL_AND_LOCAL'],
     [11640705.88235294, 'ENTERTAINMENT'],
     [10801391.298666667, 'TOOLS'],
     [9549178.467741935, 'NEWS_AND_MAGAZINES'],
     [8767811.894736841, 'BOOKS_AND_REFERENCE'],
     [7036877.311557789, 'SHOPPING'],
     [5201482.6122448975, 'PERSONALIZATION'],
     [5074486.197183099, 'WEATHER'],
     [4188821.9853479853, 'HEALTH_AND_FITNESS'],
     [4056941.7741935486, 'MAPS_AND_NAVIGATION'],
     [3697848.1731343283, 'FAMILY'],
     [3638640.1428571427, 'SPORTS'],
     [1986335.0877192982, 'ART_AND_DESIGN'],
     [1924897.7363636363, 'FOOD_AND_DRINK'],
     [1833495.145631068, 'EDUCATION'],
     [1712290.1474201474, 'BUSINESS'],
     [1437816.2687861272, 'LIFESTYLE'],
     [1387692.475609756, 'FINANCE'],
     [1331540.5616438356, 'HOUSE_AND_HOME'],
     [854028.8303030303, 'DATING'],
     [817657.2727272727, 'COMICS'],
     [647317.8170731707, 'AUTO_AND_VEHICLES'],
     [638503.734939759, 'LIBRARIES_AND_DEMO'],
     [542603.6206896552, 'PARENTING'],
     [513151.88679245283, 'BEAUTY'],
     [253542.22222222222, 'EVENTS'],
     [120550.61980830671, 'MEDICAL']]



The top five categories that have the highest number of average installs, in the Google Play Store, are:

**Communications** - 38,456,119 installs <br>
**Video Players** - 24,727,872 installs <br>
**Social** - 23,253,652 installs <br>
**Photography** - 17,840,110 installs <br>
**Productivity** - 16,787,331 installs <br>

On average, communication apps have the most installs: 38,456,119. This number is heavily skewed up by a few apps that have over one billion installs (WhatsApp, Facebook Messenger, Skype, Google Chrome, Gmail, and Hangouts), and a few others with over 100 and 500 million installs:


```python
for app in google_final:
    if app[1] == 'COMMUNICATION' and (app[5] == '1,000,000,000+'
                                      or app[5] == '500,000,000+'
                                      or app[5] == '100,000,000+'):
        print(app[0], ':', app[5])
```

    WhatsApp Messenger : 1,000,000,000+
    imo beta free calls and text : 100,000,000+
    Android Messages : 100,000,000+
    Google Duo - High Quality Video Calls : 500,000,000+
    Messenger – Text and Video Chat for Free : 1,000,000,000+
    imo free video calls and chat : 500,000,000+
    Skype - free IM & video calls : 1,000,000,000+
    Who : 100,000,000+
    GO SMS Pro - Messenger, Free Themes, Emoji : 100,000,000+
    LINE: Free Calls & Messages : 500,000,000+
    Google Chrome: Fast & Secure : 1,000,000,000+
    Firefox Browser fast & private : 100,000,000+
    UC Browser - Fast Download Private & Secure : 500,000,000+
    Gmail : 1,000,000,000+
    Hangouts : 1,000,000,000+
    Messenger Lite: Free Calls & Messages : 100,000,000+
    Kik : 100,000,000+
    KakaoTalk: Free Calls & Text : 100,000,000+
    Opera Mini - fast web browser : 100,000,000+
    Opera Browser: Fast and Secure : 100,000,000+
    Telegram : 100,000,000+
    Truecaller: Caller ID, SMS spam blocking & Dialer : 100,000,000+
    UC Browser Mini -Tiny Fast Private & Secure : 100,000,000+
    Viber Messenger : 500,000,000+
    WeChat : 100,000,000+
    Yahoo Mail – Stay Organized : 100,000,000+
    BBM - Free Calls & Messages : 100,000,000+


If we removed all the communication apps that have over 100 million installs, the average would be **reduced by approxiamtely 90.62%** to an average of **3,603,485**.


```python
under_100m_comm = []

for app in google_final:
    n_installs = app[5]
    remove = ''
        
    if '+' in app[5]:
        remove = app[5].translate({ord('+'): None})
    if ',' in app[5]:
        remove = remove.translate({ord(','): None})
    if (app[1] == 'COMMUNICATION') and (float(remove) < 100000000):
        under_100m_comm.append(float(remove))
        
sum(under_100m_comm) / len(under_100m_comm)
```




    3603485.3884615386



We see the same pattern for the video players category. The market is dominated by apps like Youtube, and Google Play. This pattern is repeated for social apps (Facebook, Instagram, Google+, etc.), photography apps (Google Photos), and productivity apps (Microsoft Word, Dropbox, and Google Docs).

**Video Players:**


```python
for app in google_final:
    if app[1] == 'VIDEO_PLAYERS' and (app[5] == '1,000,000,000+'
                                      or app[5] == '500,000,000+'
                                      or app[5] == '100,000,000+'):
        print(app[0], ':', app[5])
```

    YouTube : 1,000,000,000+
    Motorola Gallery : 100,000,000+
    VLC for Android : 100,000,000+
    Google Play Movies & TV : 1,000,000,000+
    MX Player : 500,000,000+
    Dubsmash : 100,000,000+
    VivaVideo - Video Editor & Photo Movie : 100,000,000+
    VideoShow-Video Editor, Video Maker, Beauty Camera : 100,000,000+
    Motorola FM Radio : 100,000,000+



```python
under_100m_vid = []

for app in google_final:
    n_installs = app[5]
    remove = ''
        
    if '+' in app[5]:
        remove = app[5].translate({ord('+'): None})
    if ',' in app[5]:
        remove = remove.translate({ord(','): None})
    if (app[1] == 'VIDEO_PLAYERS') and (float(remove) < 100000000):
        under_100m_vid.append(float(remove))
        
sum(under_100m_vid) / len(under_100m_vid)
```




    5544878.133333334



If we removed all the video player apps that have over 100 million installs, the average would be **reduced by approxiamtely 77.57%** to an average of **5,544,878**.

**Social:**


```python
for app in google_final:
    if app[1] == 'SOCIAL' and (app[5] == '1,000,000,000+'
                                      or app[5] == '500,000,000+'
                                      or app[5] == '100,000,000+'):
        print(app[0], ':', app[5])
```

    Facebook : 1,000,000,000+
    Facebook Lite : 500,000,000+
    Tumblr : 100,000,000+
    Pinterest : 100,000,000+
    Google+ : 1,000,000,000+
    Badoo - Free Chat & Dating App : 100,000,000+
    Tango - Live Video Broadcast : 100,000,000+
    Instagram : 1,000,000,000+
    Snapchat : 500,000,000+
    LinkedIn : 100,000,000+
    Tik Tok - including musical.ly : 100,000,000+
    BIGO LIVE - Live Stream : 100,000,000+
    VK : 100,000,000+



```python
under_100m_soc = []

for app in google_final:
    n_installs = app[5]
    remove = ''
        
    if '+' in app[5]:
        remove = app[5].translate({ord('+'): None})
    if ',' in app[5]:
        remove = remove.translate({ord(','): None})
    if (app[1] == 'SOCIAL') and (float(remove) < 100000000):
        under_100m_soc.append(float(remove))
        
sum(under_100m_soc) / len(under_100m_soc)
```




    3084582.5201793723



If we removed all the social apps that have over 100 million installs, the average would be **reduced by approxiamtely 86.73%** to an average of **3,084,582**. 

***Photography:***


```python
for app in google_final:
    if app[1] == 'PHOTOGRAPHY' and (app[5] == '1,000,000,000+'
                                      or app[5] == '500,000,000+'
                                      or app[5] == '100,000,000+'):
        print(app[0], ':', app[5])
```

    B612 - Beauty & Filter Camera : 100,000,000+
    YouCam Makeup - Magic Selfie Makeovers : 100,000,000+
    Sweet Selfie - selfie camera, beauty cam, photo edit : 100,000,000+
    Google Photos : 1,000,000,000+
    Retrica : 100,000,000+
    Photo Editor Pro : 100,000,000+
    BeautyPlus - Easy Photo Editor & Selfie Camera : 100,000,000+
    PicsArt Photo Studio: Collage Maker & Pic Editor : 100,000,000+
    Photo Collage Editor : 100,000,000+
    Z Camera - Photo Editor, Beauty Selfie, Collage : 100,000,000+
    PhotoGrid: Video & Pic Collage Maker, Photo Editor : 100,000,000+
    Candy Camera - selfie, beauty camera, photo editor : 100,000,000+
    YouCam Perfect - Selfie Photo Editor : 100,000,000+
    Camera360: Selfie Photo Editor with Funny Sticker : 100,000,000+
    S Photo Editor - Collage Maker , Photo Collage : 100,000,000+
    AR effect : 100,000,000+
    Cymera Camera- Photo Editor, Filter,Collage,Layout : 100,000,000+
    LINE Camera - Photo editor : 100,000,000+
    Photo Editor Collage Maker Pro : 100,000,000+



```python
under_100m_pho = []

for app in google_final:
    n_installs = app[5]
    remove = ''
        
    if '+' in app[5]:
        remove = app[5].translate({ord('+'): None})
    if ',' in app[5]:
        remove = remove.translate({ord(','): None})
    if (app[1] == 'PHOTOGRAPHY') and (float(remove) < 100000000):
        under_100m_pho.append(float(remove))
        
sum(under_100m_pho) / len(under_100m_pho)
```




    7670532.29338843



If we removed all the photography apps that have over 100 million installs, the average would be **reduced by approxiamtely 57.00%** to an average of **7,670,532**. 

Finally, Productivity:


```python
for app in google_final:
    if app[1] == 'PRODUCTIVITY' and (app[5] == '1,000,000,000+'
                                      or app[5] == '500,000,000+'
                                      or app[5] == '100,000,000+'):
        print(app[0], ':', app[5])
```

    Microsoft Word : 500,000,000+
    Microsoft Outlook : 100,000,000+
    Microsoft OneDrive : 100,000,000+
    Microsoft OneNote : 100,000,000+
    Google Keep : 100,000,000+
    ES File Explorer File Manager : 100,000,000+
    Dropbox : 500,000,000+
    Google Docs : 100,000,000+
    Microsoft PowerPoint : 100,000,000+
    Samsung Notes : 100,000,000+
    SwiftKey Keyboard : 100,000,000+
    Google Drive : 1,000,000,000+
    Adobe Acrobat Reader : 100,000,000+
    Google Sheets : 100,000,000+
    Microsoft Excel : 100,000,000+
    WPS Office - Word, Docs, PDF, Note, Slide & Sheet : 100,000,000+
    Google Slides : 100,000,000+
    ColorNote Notepad Notes : 100,000,000+
    Evernote – Organizer, Planner for Notes & Memos : 100,000,000+
    Google Calendar : 500,000,000+
    Cloud Print : 500,000,000+
    CamScanner - Phone PDF Creator : 100,000,000+



```python
under_100m_pro = []

for app in google_final:
    n_installs = app[5]
    remove = ''
        
    if '+' in app[5]:
        remove = app[5].translate({ord('+'): None})
    if ',' in app[5]:
        remove = remove.translate({ord(','): None})
    if (app[1] == 'PRODUCTIVITY') and (float(remove) < 100000000):
        under_100m_pro.append(float(remove))
        
sum(under_100m_pro) / len(under_100m_pro)
```




    3379657.318885449



If we removed all the productivity apps that have over 100 million installs, the average would be **reduced by approxiamtely 79.86%** to an average of **3,379,657**.

Although the **Games** category did not make the top five highest installed apps, we were curious to see if the games category would follow the same big-brand domination pattern that we saw in previous categories. As a reminder, we concluded that games were the most commonly **built** app. Games, in the App Store, however, were not a type of app that was frequently reviewed.


```python
for app in google_final:
    if app[1] == 'GAME' and (app[5] == '1,000,000,000+'
                                      or app[5] == '500,000,000+'
                                      or app[5] == '100,000,000+'):
        print(app[0], ':', app[5])
```

    Sonic Dash : 100,000,000+
    PAC-MAN : 100,000,000+
    Roll the Ball® - slide puzzle : 100,000,000+
    Piano Tiles 2™ : 100,000,000+
    Pokémon GO : 100,000,000+
    Extreme Car Driving Simulator : 100,000,000+
    Trivia Crack : 100,000,000+
    Angry Birds 2 : 100,000,000+
    Candy Crush Saga : 500,000,000+
    8 Ball Pool : 100,000,000+
    Subway Surfers : 1,000,000,000+
    Candy Crush Soda Saga : 100,000,000+
    Clash Royale : 100,000,000+
    Clash of Clans : 100,000,000+
    Plants vs. Zombies FREE : 100,000,000+
    Pou : 500,000,000+
    Flow Free : 100,000,000+
    My Talking Angela : 100,000,000+
    slither.io : 100,000,000+
    Cooking Fever : 100,000,000+
    Yes day : 100,000,000+
    Score! Hero : 100,000,000+
    Dream League Soccer 2018 : 100,000,000+
    My Talking Tom : 500,000,000+
    Sniper 3D Gun Shooter: Free Shooting Games - FPS : 100,000,000+
    Zombie Tsunami : 100,000,000+
    Helix Jump : 100,000,000+
    Crossy Road : 100,000,000+
    Temple Run 2 : 500,000,000+
    Talking Tom Gold Run : 100,000,000+
    Agar.io : 100,000,000+
    Bus Rush: Subway Edition : 100,000,000+
    Traffic Racer : 100,000,000+
    Hill Climb Racing : 100,000,000+
    Angry Birds Rio : 100,000,000+
    Cut the Rope FULL FREE : 100,000,000+
    Hungry Shark Evolution : 100,000,000+
    Angry Birds Classic : 100,000,000+
    Hill Climb Racing 2 : 100,000,000+
    Jetpack Joyride : 100,000,000+
    Super Mario Run : 100,000,000+
    Glow Hockey : 100,000,000+
    Asphalt 8: Airborne : 100,000,000+
    Lep's World 2 🍀🍀 : 100,000,000+
    Fruit Ninja® : 100,000,000+
    Vector : 100,000,000+
    Dr. Driving : 100,000,000+
    Bike Race Free - Top Motorcycle Racing Games : 100,000,000+
    Smash Hit : 100,000,000+
    Temple Run : 100,000,000+
    Geometry Dash Lite : 100,000,000+
    Ant Smasher by Best Cool & Fun Games : 100,000,000+
    Angry Birds Star Wars : 100,000,000+
    Mobile Legends: Bang Bang : 100,000,000+
    Banana Kong : 100,000,000+
    Skater Boy : 100,000,000+
    Shadow Fight 2 : 100,000,000+
    Modern Combat 5: eSports FPS : 100,000,000+
    Garena Free Fire : 100,000,000+



```python
under_100m_game = []

for app in google_final:
    n_installs = app[5]
    remove = ''
        
    if '+' in app[5]:
        remove = app[5].translate({ord('+'): None})
    if ',' in app[5]:
        remove = remove.translate({ord(','): None})
    if (app[1] == 'GAME') and (float(remove) < 100000000):
        under_100m_game.append(float(remove))
        
sum(under_100m_game) / len(under_100m_game)
```




    6272564.694894147



If we removed all the game apps that have over 100 million installs, the average would be **reduced by approxiamtely 59.76%** to an average of **6,272,564**. The pattern of domination did continue. 

Again, the main concern is that these app genres might seem more popular than they are. These niches seem to be dominated by large companies who are hard to compete against.

---
---

## CONCLUSION

After observing that the top 10 Google Play categories were all highly big-brand dominated, we realized that we could not simply look for a category that had little to no evident dominace. If we did, we might end up recommending a category that just does not have the level of natural engagement that our company needs to bring in revenue. 

So we changed our approach and looked for categories that had a moderate levels of installations, moderate levels of big-brand dominance, and a diverse range of sub-categories. Hopefully we would be able to find a fairly popular category that has a sub-catagories that have room for expansion. 


```python
for app in google_final:
    if app[1] == 'BOOKS_AND_REFERENCE' and (app[5] == '1,000,000,000+'
                                      or app[5] == '500,000,000+'
                                      or app[5] == '100,000,000+'):
        print(app[0], ':', app[5])

```

    Google Play Books : 1,000,000,000+
    Bible : 100,000,000+
    Amazon Kindle : 100,000,000+
    Wattpad 📖 Free Books : 100,000,000+
    Audiobooks from Audible : 100,000,000+


The **Books and Reference** category has only 5 large competitiors, with installs over 100 million. 


```python
for app in google_final:
    if app[1] == 'BOOKS_AND_REFERENCE' and (app[5] == '10,000,000+'):
        print(app[0], ':', app[5])
```

    Wikipedia : 10,000,000+
    Cool Reader : 10,000,000+
    FBReader: Favorite Book Reader : 10,000,000+
    HTC Help : 10,000,000+
    Moon+ Reader : 10,000,000+
    Aldiko Book Reader : 10,000,000+
    Al-Quran (Free) : 10,000,000+
    Al Quran Indonesia : 10,000,000+
    Al'Quran Bahasa Indonesia : 10,000,000+
    Quran for Android : 10,000,000+
    Dictionary.com: Find Definitions for English Words : 10,000,000+
    English Dictionary - Offline : 10,000,000+
    NOOK: Read eBooks & Magazines : 10,000,000+
    Dictionary : 10,000,000+
    Spanish English Translator : 10,000,000+
    Dictionary - Merriam-Webster : 10,000,000+
    JW Library : 10,000,000+
    Oxford Dictionary of English : Free : 10,000,000+
    English Hindi Dictionary : 10,000,000+


Apps with installations over 10 million fall into the **Dictionary**, **Religious Texts**, **Libraries** and **E-Reader** sub-categories. 

We observed that multiple apps were built around the book Quran, which suggests that building an app around a globally read book (maybe religious text) could potentially generate the level of engagement the company needs to bring in revenue. 

A more specific suggestion would be to create a library that allows the reader to read globaly popular boook, and search for the defition of unknow words in the app. The reader could receive both a dictionary definition and an etymological history of the word's use. 

A book/reference app seems like it would be able to generate revenue in both the Google Play and App Store markets. This category ranked moderately high ranking of 11th, when comparing installs in the Google Play Store. But Reference was the second highest reviewed genre in the App Store; books ranked 6th. Ultimately the development team will have to create an app with features different enough from other like-apps, to rise above potential competition. 


```python

```
