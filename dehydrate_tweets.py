# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 18:40:33 2020

Python script to dehydrate the tweets ids from tweets folder collected with
Tweet_wrapper_v2.py from the repository Huertas97/tweets_collection GitHub

@author: Álvaro Huertas García
"""

import pandas as pd
import os
import sys
from tqdm.auto import tqdm
import logging
logging.basicConfig(format='%(asctime)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.INFO)
from optparse import OptionParser
# Process command-line options
parser = OptionParser(add_help_option=False)

# General options
parser.add_option('--tweets_path', type='str', help='Number of sentences to retrieve')
parser.add_option('--output_name', type='str', default = "dehydrated_tweets", help='Number of sentences to retrieve')
parser.add_option('--help', action='store_true', help='Show this help message and exit.')

(options, args) = parser.parse_args()


def print_usage():
    print("""       
Python script to dehydrate the tweets ids from tweets folder collected with
Tweet_wrapper_v2.py from the repository Huertas97/tweets_collection GitHub

        
Usage:

     python dehydrate_tweets.py [options] 

Options:
    --tweets_path                Path where the tweets to dehydrate are located
    --output_name                Name for folder where dehydrated results will be stored. Default: "dehydrated_tweets"
    --help                       Help documentation
    
Example:
    $ python dehydrate_tweets.py --tweets_path tweets/ --output_name dehydrated_output
""")
    sys.exit()

if not all([options.tweets_path]) or options.help:
    print_usage()



# Path where the tweet to dehydrate are 
PATH_input_files = options.tweets_path # "tweets/"
output_folder = options.output_name
# Take the root, folders and files in current directory
for i in os.walk(PATH_input_files):
    root, folders, files = i
    if len(root) != 0 and len(files) != 0:
        print()
        logging.info("------------- Dehydrating files from folder {} -------------".format(root))
        for file in tqdm(files, desc = "Files to dehydrate"):
            try:
                # Read json with pandas
                df = pd.read_json(os.path.join(root, file))
            
                # Create folders for save dehydrated files
                PATH_output = os.path.join(output_folder, root)
                os.makedirs(PATH_output, exist_ok = True)
            
                # Create and save the output file
                dehydrated_file_name = file.replace(".json", ".txt")
                output_file = os.path.join(PATH_output, dehydrated_file_name)
                # From data frame to txt
                df.tweet_id.to_csv(output_file, header=None, index=None, sep=' ')
            except:
                print()
                logging.info("------------- Dehydration not possible for {}  -------------".format(file))
                print()