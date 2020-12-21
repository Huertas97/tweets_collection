# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 16:06:13 2020

Python script to hydrate the tweets ids from tweets folder collected in this
Huertas97/tweets_collection GitHub. The workflow is based on the idea of
passing in an iterator of tweet ids and getting back an iterator for the
decoded JSON for each corresponding tweet. 


Requirements: 
    Key, secret key, access token and secret access token to Twitter API
    Request these credentials in https://developer.twitter.com/en/docs/twitter-api
    
@author: Álvaro Huertas García
"""

import tweepy
import os
import sys
import json
from requests_oauthlib import OAuth1Session
from collections import defaultdict
from optparse import OptionParser
from tqdm.auto import tqdm
import datetime
import logging

# Process command-line options
parser = OptionParser(add_help_option=False)

# General options
parser.add_option('--api_key', type='str', help='Consumer key')
parser.add_option('--api_secret_key', type='str', help='Consumer secret key')
parser.add_option('--access_token', type='str', help='Access token')
parser.add_option('--access_token_secret', type='str', help='Secret access token')
parser.add_option('--tweets_path', type='str', help='Path where the tweets to dehydrate are located')
parser.add_option('--help', action='store_true', help='Show this help message and exit.')

(options, args) = parser.parse_args()

def print_usage():
    print("""       
Python script to hydrate the tweets ids from tweets folder collected in this
Huertas97/tweets_collection GitHub


Requirements: 
    Key, secret key, access token and secret access token to Twitter API
    Request these credentials in https://developer.twitter.com/en/docs/twitter-api
        
Usage:

     python hydrate_tweets.py [options] 

Options:
    --api_key                    CONSUMER_KEY
    --api_secret_key             CONSUMER_SECRET
    --access_token               ACCESS TOKEN   
    --access_token_secret         ACCESS TOKEN SECRET
    --tweets_path                Path where the tweets to dehydrate are located
    --help                       Help documentation

Example. 
    $ python hydrate_tweets.py --api_key XXX --api_secret_key XXX --access_token XXX \\
        --access_token_secret XXX --tweets_path tweets/
""")
    sys.exit()

if not all([options.api_key, options.api_secret_key,
            options.access_token, options.access_token_secret,
            options.tweets_path
            ]) or options.help:
    print_usage()
 


logging.basicConfig(format='%(asctime)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.INFO)

def process_time(api):
    """
    Función encargada de extraer el nº de request restantes permitidas por
    la API de Twitter. También indica cuando se renueva la ventana temporal
    para continuar la extracción de tweets.

    Parameters
    ----------
    api : API object
        sesión de la API

    Returns
    -------
    None.

    """
    # Get the number of remaining requests
    remaining = int(api.last_response.headers['x-rate-limit-remaining'])
    logging.info("Remaining requests: {}".format(remaining))
    reset = int(api.last_response.headers['x-rate-limit-reset'])
    reset = datetime.datetime.fromtimestamp(reset)
    logging.info("New requests available at: {}".format(reset))

api_key = options.api_key
api_secret_key = options.api_secret_key
access_token = options.access_token
access_token_secret = options.access_token_secret

twitter = OAuth1Session(api_key,
                        client_secret=api_secret_key,
                        resource_owner_key=access_token,
                        resource_owner_secret=access_token_secret)
auth = tweepy.AppAuthHandler(api_key, api_secret_key)
api = tweepy.API(auth, wait_on_rate_limit=True) 



PATH_input_files= options.tweets_path # "tweets/"
PATH_hydrated = "hydrated_files/"

# Take the root, folders and files in current directory
for i in os.walk(PATH_input_files):
    root, folders, files = i
    
    # If the root exist and there are files we are in a
    # date subfolder with a file per Twitter user to hydrate
    if len(root) != 0 and len(files) != 0:
        
        # Hydrate the tweet ids for a Twitter user
        print()
        logging.info("--------- Hydrating files from folder {} -----------".format(root))
        for file_name in tqdm(files, desc = "Files hydrated"):
            # print()
            # print(file_name)
            file_path = os.path.join(root, file_name)
            
            # Read and hydrate the ids file in batches of 100 ids
            with open(file_path, "r") as f:
                tweet_ids = []          
                dd = defaultdict(list)     # Dictionary to append the metadata from each tweet id
                for id_ in f.readlines():
                    tweet_ids.append(id_.strip())

                    # List of ids must be up to 100 
                    if len(tweet_ids) == 100: 
                        statuses = api.statuses_lookup(tweet_ids, tweet_mode="extended")
                        l_metadata = [status._json for status in statuses]

                        # Add to a dict Hydrated metadata in th
                        for metadata in l_metadata: 
                            for key, value in metadata.items():
                                dd[key].append(value)
                        # If a batch has been hydrated reset bactch
                        tweet_ids = []
                
                # If the nº of ids is lower than 100
                if len(tweet_ids) > 0:
                   statuses = api.statuses_lookup(tweet_ids, tweet_mode="extended")
                   l_metadata = [status._json for status in statuses]
                   
                   # Add to a dict Hydrated metadata in th
                   for metadata in l_metadata: 
                       for key, value in metadata.items():
                           dd[key].append(value)
                   
                

            # Create the output folder
            hydrated_file_name  = "hydrated_" + file_name.replace(".txt", ".json")
            PATH_output = os.path.join(PATH_hydrated, root)
            os.makedirs(PATH_output, exist_ok = True)
            # Create the hydrate json file in the output folder
            output_file = os.path.join(PATH_output, hydrated_file_name)
            with open(output_file, 'w') as outfile:
                    json.dump(dd, outfile)
            
            # Mostramos el nº de request y ventana temporal disponible en la API
            print()
            process_time(api)