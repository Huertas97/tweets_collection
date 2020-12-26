# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 15:07:00 2020


This scripts uploads JSON files from hydrated tweets to a MongoDB collection.
The user should have a MongoDB user name, password, database and collection to
upload the hydrated data. A filter option si available in case the user only want 
to upload data from Fact-checkers. Be aware of the limitations of your 
MongoDB database according to the instance type. For example a free database 
(M0 instance type) has a limitation of 512 MB available for storage.


@author: Álvaro Huertas García 
"""

import os
import sys
import json
from pymongo import MongoClient
from optparse import OptionParser
# Process command-line options
parser = OptionParser(add_help_option=False)

# General options
parser.add_option('-p', '--path', type="str", default="../local_tweets", help='Path to json files to upload to MongoDB')
parser.add_option('-h', '--help', action='store_true', help='Show this help message and exit.')
parser.add_option('-f', '--filter', action='store_true', help='Apply filter to upload only Fact-checkers tweets')
parser.add_option('--mongo_user', type='str', help="MongoDB user")
parser.add_option('--mongo_pass', type='str', help="MongoDB password")
parser.add_option('--mongo_dbname', type='str', help="MongoDB database name")
parser.add_option('--mongo_collection', type='str', help="MongoDB collection name")

(options, args) = parser.parse_args()

# Example of use: 
#     python upload_mongo.py --mongo_user Huertas97 
#                            --mongo_pass 32pass23UAM 
#                            --mongo_dbname fact-check-tweet-collection 
#                            --mongo_collection tweets 
#                            --path ..\Recopilacion_teetws_PC\local_tweets\
    
def print_usage():
    print("""
Information:
    This scripts uploads JSON files from hydrated tweets to a MongoDB collection.
    The user should have a MongoDB user name, password, database and collection to
    upload the hydrated data. A filter option si available in case the user only want 
    to upload data from Fact-checkers. 

Usage: 
     python upload_mongo.py  [options]

Options:
    -p, --path                   Path were the JSON file to upload are located
    -f  --filter                 Apply filter to upload only Fact-checkers tweets
    -h  --help                   Show help documentation
    --mongo_user                 MongoDB user
    --mongo_pass                 MongoDB password
    --mongo_dbname               MongoDB databse name
    --mongo_collection           MongoDB collection name


Example. 

Upload to MongoDB files only from fact-checkers
    $ python upload_mongo.py --filter --mongo_user Huertas97 --mongo_pass XXX \
        --mongo_dbname fact-check-tweet-collection --mongo_collection tweets \
        --path ..\local_tweets\ 

Upload to MongoDB files (no filters)
    $ python upload_mongo.py --mongo_user Huertas97 --mongo_pass XXX \
        --mongo_dbname fact-check-tweet-collection --mongo_collection tweets \
        --path ..\local_tweets\                 
        """)
    sys.exit() 
    
if options.help:
    print_usage() 

def extract_checked(file_name, checked_users):
    user = file_name.split("-")[0]
    if user in checked_users:
        return True
    else:
        return False

def json2dic(file_name, root):
    file_path = os.path.join(root, file_name)
    with open(file_path) as f:
        data = json.load(f)
    return data



# Only Fact--checker Twitter accounts will be saved on MongoDB
checked_users = ['malditobulo',
                'maldita_ciencia',
                'EFEVerifica',
                'Chequeado',
                'Newtral',
                'FullFact',
                'ElSabuesoAP',
                'cotejoinfo',
                'ECUADORCHEQUEA',
                'lasillavacia',
                'AP',
                'AfricaCheck',
                'aosfatos',
                'AAPNewswire',
                'boomlive_in',
                'correctiv_org',
                'Check_Your_Fact',
                'CheckCongo',
                'DemagogPL',
                'dubawaNG',
                'estadaoverifica',
                'FactlyIndia',
                'FactCrescendo',
                'FactCheckNI',
                'ghana_fact',
                'Fatabyyano_com',
                'FerretScot',
                'Observateurs',
                'lemondefr',
                'CheckNewsfr',
                'LogicallyAI',
                'MaharatNews',
                'Poynter',
                'mediawise',
                'NewsMobileIndia',
                'NewsMeter_In',
                'observadorpt',
                'PesaCheck',
                'JornalPoligrafo',
                'ABCFactCheck',
                'rapplerdotcom',
                'ReutersAgency',
                'ClimateFdbk',
                'eye_digit',
                'SouthAsiaCheck',
                'StopFakingNews',
                'IndiaToday',
                'factchecknet',
                'thedispatch',
                'ThipMedia',
                'TheQuint',
                'GlennKesslerWP',
                'thejournal_ie',
                'USATODAY',
                'verafiles',
                'newsvishvas',
                'dpa',
                'dogrulukpayicom',
                'PagellaPolitica',
                'teyitorg',
                'NUnl',
                'snopes',
                'franceinfo']
data_list = []
PATH_input_files= options.path
# Upload
mongo_user = options.mongo_user
mongo_pass = options.mongo_pass
mongo_dbname = options.mongo_dbname
mongo_collection = options.mongo_collection
client = MongoClient("mongodb+srv://" + mongo_user + ":" +
                             mongo_pass + "@fact-check-tweet-collec.oaort.mongodb.net/" + 
                             mongo_dbname + "?retryWrites=true&w=majority")
db = client[mongo_dbname] 
collection = db[mongo_collection]
# Take the root, folders and files in current directory
for i in os.walk(PATH_input_files):
    root, folders, files = i
    # If the root exist and there are files we are in a
    # date subfolder with a file per Twitter user to hydrate
    if len(root) != 0 and len(files) != 0:
        print("Uploading JSON files from {}".format(root))
        
        # Filter files if desired
        if options.filter:
            files = filter(lambda f: extract_checked(f, checked_users), files) 
            
        # Extract content as a dictionary to upload. List of data
        data_checked = list(map(lambda f: json2dic(f, root), files))
        
        # Upload the data extracted for a folder (date)
        collection.insert_many(data_checked)
