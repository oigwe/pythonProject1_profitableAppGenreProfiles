opened_file_apple = open('/data_sets/AppleStore.csv')
from csv import reader 
read_file_apple = reader(opened_file_apple) 
apps_data_apple = list(read_file_apple)

opened_file_google = open('/data_sets/googleplaystore.csv')
from csv import reader 
read_file_google = reader(opened_file_google) 
apps_data_google = list(read_file_google)