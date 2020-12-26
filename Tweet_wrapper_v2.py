#!/usr/bin/env python
# coding: utf-8

"""
Created on Sun Dec 20 18:40:33 2020

This script allows the user to collects dehydrated and hydrated tweets from
Twitter accounts.The default Twitter accounts were selected by hand. 
Feel free to change the ones selected in this script. Tweets extractions is
accomplish using Tweepy. More information in print_usage().

Requirements:
     -> tweepy             (pip install -U -q tweepy)
     -> emoji              (pip install -U -q emoji)
     -> github             (pip install -U -q PyGithub)
     -> tqdm               (pip install -U -q tqdm)
     -> requests_oauthlib  (pip install -U -q requests-oauthlib)
     -> pymongo            (pip install pymongo)
     
Furthermore, you should have a GitHub account and a Twitter Developer API 
credentials. Contact me if you want to use our Twitter API. 

@author: Álvaro Huertas García
"""
# !pip install -U -q tweepy
# !pip install -U -q emoji
# !pip install -U PyGithub
# !pip install -U -q tqdm

import pandas as pd
import time
import datetime
import os
from optparse import OptionParser
import sys
import json
from pymongo import MongoClient


try:
    import tweepy
    import emoji
    from github import Github
    from github import InputGitAuthor
    from tqdm import tqdm
    from requests_oauthlib import OAuth1Session
    
except ImportError as error:
    print(error)
    print("""Requirements:
          -> tweepy             (pip install -U -q tweepy)
          -> emoji              (pip install -U -q emoji)
          -> github             (pip install -U -q PyGithub)
          -> tqdm               (pip install -U -q tqdm)
          -> requests_oauthlib  (pip install -U -q requests-oauthlib)
          -> pymongo            (pip install pymongo)""")
    sys.exit()
    

# Process command-line options
parser = OptionParser(add_help_option=False)

# General options
parser.add_option('-h', '--help', action='store_true', help='Show this help message and exit.')
parser.add_option('-t', '--today', action='store_true', help='Collect tweets from today')
parser.add_option('-d', '--day', type='int',  help='Number of days to go back in time to collect tweets')
parser.add_option('-c', '--count', type= 'int', help = 'Number of tweets collected per user. Directly related with computing time.')
parser.add_option("--tweets_source_info", action = 'store_true', help = "Information. Show the Twitter accounts used for the tweets extraction")
parser.add_option("--git_token",  type= "str", help = "Token needed to access the Github repository where the results will be saved")
parser.add_option("--git_repo",  type = "str", help = "Repository where you want to save the json file generated after tweet extraction")
parser.add_option("--git_autor",  type = "str", help = "GitHub changes author")
parser.add_option("--git_autor_email", type = "str", help = "E-mail from the author")
parser.add_option('--api_key', type='str', help='Consumer key')
parser.add_option('--api_secret_key', type='str', help='Consumer secret key')
parser.add_option('--access_token', type='str', help='Access token')
parser.add_option('--access_token_secret', type='str', help='Secret access token')
parser.add_option('--save_local', action='store_true', help='Bool. If data should be save locally')
parser.add_option('--local_path', type="str", default ="../local_tweets/", help='Bool. If data should be save locally')
parser.add_option('--mongo_user', type='str', help="MongoDB user")
parser.add_option('--mongo_pass', type='str', help="MongoDB password")
parser.add_option('--mongo_dbname', type='str', help="MongoDB database name")
parser.add_option('--mongo_collection', type='str', help="MongoDB collection name")

(options, args) = parser.parse_args()

def print_usage():
    print("""
Information:
    This script allows the user to collects dehydrated and hydrated tweets from
    Twitter accounts. The user has several options to save the data extracted: 
    locally, on GitHub, on MongoDB. To save locally use --save_local and --local_path
    commands. To save on GitHub use --git_token and --git_repo commands. To save
    the data on MongoDB use --mongo_user, --mongo_pass, --mongo_dbname, --mongo_collection.
    
    
    The default Twitter accounts were selected by hand. 
    Feel free to change the ones selected in this script. Tweets extractions is
    accomplish using Tweepy. Hydrated tweets are saved locally. Dehydrated tweets
    are the ones uploaded to GitHub. Nevertheless, the user decides if tweets
    should be saved locally (and the path desired) or saved on GitHub (and the
    repository desired). 
    
    Be aware of the "Rate Limits" from Twitter. Among these limits, the number of
    tweet extraction requests is up to 450 in a temporal window of 15 minutes. 
    Once the temporal windows ends, the number of requests are restarted.
    Nevertheless, the code has been developed to manage and inform about these
    temporal windows and to continue the tweets extraction. 
    
    Moreover, you should be aware that Twitter Policy only allows to extract 
    tweets within the las 7 days (30 days for Premium API).  

    The tweets collected are saved as json files. The Twitter accounts without
    tweets available for the date selected do not create json files. The information
    saved in the json files are the following ones: 
        - account name
        - tweet id
        - full text (both tweet and retweet)
        - verification of the account
        - tweet date creation
        - nº of times retweeted
        - favourites count
        - tweet location (if available)
        - account url 
        - tweet entities (url, hastags, etc)

Usage: 
    python Tweet_wrapper_v2.py [options]

Options:
    -t, --today                  Collect tweets from today
    -d, --day                    Number of days to go back in time to collect tweets. Ex: 1 = yesterday.
    -c, --count                  Number of tweets collected per user. Directly related with computing time. Default: 200 
    --git_token                  Token needed to access the Github repository where the results will be saved
    --git_repo                   Repository where you want to save the json file generated after tweet extraction
    --tweets_source_info         Information. Show the Twitter accounts used for the tweets extraction
    --git_autor                  GitHub changes author
    --git_autor_email            E-mail author
    --api_key                    CONSUMER_KEY
    --api_secret_key             CONSUMER_SECRET
    --access_token               ACCESS TOKEN   
    --access_token_secret        ACCESS TOKEN SECRET
    --save_local                 Bool. If data should be save locally
    --local_path                 Path to save data locally. Default: "../local_tweets/"
    --mongo_user                 MongoDB user
    --mongo_pass                 MongoDB password
    --mongo_dbname               MongoDB databse name
    --mongo_collection           MongoDB collection name
    
Requirements:
     -> tweepy             (pip install -U -q tweepy)
     -> emoji              (pip install -U -q emoji)
     -> github             (pip install -U -q PyGithub)
     -> tqdm               (pip install -U -q tqdm)
     -> requests_oauthlib  (pip install -U -q requests-oauthlib)
     -> pymongo            (pip install pymongo)
     
     Furthermore, you should have a GitHub account and a Twitter Developer API
     credentials. 

Example. 

Collect up to 100 tweets from today, save them locally and on GitHub:
    $ python Tweet_wrapper_v2.py -t -c 100 \
        --save_local --local_path "../local_tweets" \
        --git_token XXX --git_repo Huertas97/tweets_collection \
        --api_key XXX --api_secret_key XXX --access_token XXX --access_token_secret 
        
Collect up to 200 tweets from yesterday, save them locally (not GitHub): 
    $ python Tweet_wrapper_v2.py -d 1 -c 200 \
        --save_local --local_path "../local_tweets" \
        --api_key XXX --api_secret_key XXX --access_token XXX --access_token_secret  

Collect up to 40 tweets from 4 days ago, save them locally and on MongoDB (not GitHub): 
    $ python Tweet_wrapper_v2.py -d 4 -c 40 \
        --save_local --local_path "../local_tweets" \
        --mongo_user Huertas97 --mongo_pass XXX  \
        --mongo_dbname fact-check-tweet-collection \
        --mongo_collection tweets
        --api_key XXX --api_secret_key XXX --access_token XXX --access_token_secret
        """)
    sys.exit()



def process_time(api):
    """
    Function in charge of extracting the remaining number of requests allowed by
    the Twitter API. It also indicates when the time window is renewed
    to continue the tweet extraction.

    Parameters
    ----------
    api : API object
        API session

    Returns
    -------
    None.

    """
    # Get the number of remaining requests
    remaining = int(api.last_response.headers['x-rate-limit-remaining'])
    print("Remaining requests:", remaining)
    reset = int(api.last_response.headers['x-rate-limit-reset'])
    reset = datetime.datetime.fromtimestamp(reset)
    print("Requests reset at: ", reset)

def tweet_collect(user_name, text_query, since_date,  count, language, result_type):
    """
    Function in charge of making the request to Twitter of a user and collect his
    tweets.

    Parameters
    ----------
    user_name : string
        Twitter account name
    text_query : string
        Filtros que aplicar a la búsqueda. Ej. "from: Usuario" solo busca en
        ese usuario
    since_date: datetime
        Filters to apply to the search. E.g. "from: User" only searches in
        that user
    count : int, optional
        Nº of tweets to extract. The default is 200
    language : string, optional
        Language filter. The default is "es".

    Returns
    -------
    tweets_df : pandas data frame
        Data Frame containing tweets in the rows and columns: the id,
        the full text, account verification, creation date,
        the location of the account url and the entities of each tweet
        extracted.

    """
    
    query = text_query + user_name
    

    
    print("\nCollecting tweets from user {0}, date: {1}".format(user_name, since_date.date()))
    next_day = since_date  + datetime.timedelta(1)
    try:
        # Creation of query method using parameters
        tweets = tweepy.Cursor(api.search,
                               q=query,
                               lang=language,
                               tweet_mode='extended',
                               result_type = result_type,
                               until = next_day.date()
                               ).items(count)
        
        # Teets info extraction
        tweets_list = []
        for tweet in tweets:
            if  since_date.date() == tweet.created_at.date():
                # Fulltext (both retweet or tweet)
                if 'retweeted_status' in tweet._json:
                    is_retweet = True
                    full_text = tweet._json['retweeted_status']['full_text']
                else:
                    is_retweet = False
                    full_text = tweet.full_text
                tweets_list.append([tweet.user.screen_name,
                                        tweet.id,
                                        is_retweet,
                                        full_text,
                                        tweet.user.verified,
                                        str(tweet.created_at),
                                        tweet.retweet_count, 
                                        tweet.favorite_count,
                                        #  tweet.reply_count, 
                                        # tweet.retweeted_status,
                                        tweet.user.location,
                                        tweet.user.url,
                                        tweet.entities
                                        ])
        # We show the request number and available time window from the API
        process_time(api)
        # Data frame creation
        print("Number of tweets collected:", len(tweets_list))
        if len(tweets_list) != 0:
            # Creation of dataframe from tweets list
            tweets_df = pd.DataFrame(tweets_list, columns=["screen_name",
                                                           "tweet_id",
                                                           "is_retweet",
                                                           "text",
                                                           "user_verified",
                                                           "created_at",
                                                           "retweet_count",
                                                           "favorite_count",
                                                          #  "reply_count",
                                                          # "retweet_status",
                                                           "user_location",
                                                           "user_url",
                                                           "entities"])
            # Procesamos los emojis a unicode
            tweets_df["text"] = tweets_df["text"].apply(emoji.demojize)
            
            return tweets_df
        else:
            pass

    except BaseException as e:
        print('failed on_status,', str(e))
        time.sleep(3)


def push(path, message, content, author, author_mail, branch = "main"):
    """
    Function in charge of uploading the dehydrated TXT files to GitHub.

    Parameters
    ----------
    path : string
        File path to upload to GitHub.
    message : string
        Commit message
    content : json
        TXT file content
    branch : string, optional
        Branch to push TXT file. The default is "main".

    Returns
    -------
    None.

    """
    author = InputGitAuthor(
        author,
        author_mail
    )
    try:   # If file already exists, update it
        # Retrieve old file to get its SHA and path
        contents = repo.get_contents(path, ref=branch)
        repo.update_file(contents.path,
                         message,
                         content,
                         contents.sha,
                         branch=branch,
                         author=author)  # Add, commit and push branch
        print("Update:", path)
        print()
    except:    # If file doesn't exist, create it
        repo.create_file(path,
                         message,
                         content,
                         branch=branch,
                         author=author)  # Add, commit and push branch
        print("Creating:", path)
        print()


# Number of option arguments. First arguments is always the own file name
numOpts = len(sys.argv)

# No options... print help.
if numOpts < 2:
    print_usage()
elif options.help:
    print_usage()
    
# Twiiter Accounts
dic_user = {
    # Hastags
    "Plandemia": ["es", "#", "mixed"],
    "yonomeconfino": ["es", "#", "mixed"],
    "coronatimo": ["es", "#", "mixed"],
    "YoNoMeVacuno": ["es", "#", "mixed"],
    "covid1984": ["es", "#", "mixed"],
    "NoalaVacuna": ["es", "#", "mixed"],
    "#VirusChino": ["es", "#", "mixed"],
    "#VacunaRusa": ["es", "#", "mixed"],
    "#PCRFraude": ["es", "#", "mixed"],
    "#FactCHAT": ["en", "#", "mixed"],
    "#FakePCR": ["es", "#", "mixed"],
    # infodemia 
    
    
    # Not checked
    "No__Plandemia": ["es", "from:"],
    "ANTIMASCARILLA": ["es", "from:"],
    "FoxMuld88326271": ["es", "from:"],
    "PericoAFuego": ["es", "from:"],
    "DiegoMo53772865": ["es", "from:"],
    "the_raven77": ["es", "from:"],
    "LRsecreta": ["es", "from:"],
    "JL_MDesconocido": ["es", "from:"],
    "AtraviesaLoDesc": ["es", "from:"],
    "HomeopatiaY": ["es", "from:"],
    "NaturopatasCol": ["es", "from:"],
    "MiHerbolario": ["es", "from:"],
    "HerbolarioLola": ["es", "from:"],
    "PacienteL": ["es", "from:"],
    "elphabaz": ["es", "from:"],
    "IsTortugo": ["es", "from:"],
    "tecn_preocupado": ["es", "from:"],
    "BabylonDab": ["es", "from:"],
    "lamjort": ["es", "from:"],
    "VaccineXchange": ["en", "from:"],
    "gonzo_blogger": ["es", "from:"],
    "CarmCerb21": ["es", "from:"],
    "panguerrera1": ["es", "from:"],
    "AlbaGar74381296": ["es", "from:"],
    "MediterraneoDGT": ["es", "from:"],
    "JosPastr": ["es", "from:"],
    "velardedaoiz2": ["es", "-filter:replies AND-filter:retweet AND from:"],
    "JordiFlynn": ["es", "(coronavirus OR cov OR covid OR sars) AND from:"],
    "mitokondriac": ["es", "from:"],
    "AquAhora1": ["es", "from:"],
    "patrilaselma": ["es", "from:"],
    "doctor_papaya": ["es", "from:"],
    "Autnomacabread1": ["es", "(virus OR coronavirus OR covid OR sars) AND from:"],
    "LaRetuerka": ["es", "from:"],
    "DathosBD": ["es", "-filter:replies AND (virus OR coronavirus OR covid OR sars) AND from:"],
    "PorunChileDigno": ["es", "-filter:replies AND from:"], # Chile
    "1333Despierta": ["es", "-filter:replies AND from:"],
    "NoHayPandemia__": ["es", "-filter:replies AND from:"],
    "Musicolorista": ["es", "-filter:replies AND from:"],
    "ELMINIMALISTA1": ["es", "-filter:replies AND from:"],
    "Africamar": ["es", "-filter:replies  AND from:"],
    "informate_infor": ["es", "-filter:replies  AND from:"],
    "ElTrompetista78": ["es", "-filter:replies  AND from:"],
    "Angelisimo2": ["es", "-filter:replies  AND from:"],
    "_nWorder": ["es", "-filter:replies  AND from:"],
    "papayaykware": ["es", "-filter:replies  AND from:"],
    "trustdall271": ["es", "-filter:replies AND from:"],
    "elentirvigo": ["es", "-filter:replies AND from:"],
    "ProgreAzote": ["es", "-filter:replies AND from:"],
    "The_Cling_On": ["en", "from:"], # Australia
    
    
    # Satire
    "elmundotoday": ["es", "from:"],
    "eljueves": ["es", "from:"],
    "okdiario": ["es", "from:"],
    "LaVozdelBecario": ["es", "from:"],
    "HayNoticia": ["es", "from:"],
    "FrayJosepho": ["es", "from:"],
    "ChiguireBipolar": ["es", "from:"], # Venezuela
    "actualidadpanam": ["es", "from:"],# Colombia
    "revisbarcelona": ["es", "from:"],# Argentina
    "thecliniccl": ["es", "from:"],# Chile
    "TheBabylonBee": ["en", "from:"], # US 
    "TheOnion": ["en", "from:"], # US 
    
    
    
    # Doubtful
    "tiramillas": ["es", "from:"],
    "20m": ["es", "from:"],
    "ActualidadRT": ["es", "from:"],
    "ldpsincomplejos": ["es", "-filter:replies AND from:"],
    "hermanntertsch": ["es", "-filter:replies AND -filter:retweet AND from:"],
    "NiusDiario": ["es", "from:"], # no es tan dudoso pero habría que chequear
    "LaVozIberica": ["es", "from:"],
    "periodistadigit": ["es", "from:"],
    "CancerIntegral": ["es", "from:"],
    
    # Donald Trump in Spanish
    "POTUS_Trump_ESP": ["es", "-filter:replies AND -filter:retweet AND from:"],
    
    # Institutions
    "SaludPublicaEs": ["es", "from:"],
    "sanidadgob": ["es", "from:"],
    "andaluciadatos": ["es", "from:"],
    "opsoms": ["es", "from:"],
    "WHO": ["en", "from:"],
    "AEMPSGOB": ["es", "from:"],  # spanish drug agency
    "FDAenEspanol": ["es", "from:"],
    "CDCespanol": ["es", "from:"],
    "policia": ["es", "from:"],
    "guardiacivil": ["es", "from:"],
    "US_FDA": ["en", "from:"],
    "FDA_Drug_Info": ["en", "from:"],
    "FDArecalls": ["en", "from:"],
    "CDCgov": ["en", "from:"],
    "NIH": ["en", "from:"],
    "NEJM": ["en", "from:"],
    "HopkinsMedicine": ["en", "from:"],
    "MayoClinic": ["en", "from:"],
    
    # Scientific magazines
    "NatureComms": ["en", "from:"],
    "researchnews": ["en", "from:"],
    "CellPressNews": ["en", "from:"],
    "TrendsMolecMed": ["en", "from:"],
    "embojournal": ["en", "from:"],
    
    # Fact-checkers
    "malditobulo": ["es", "from:"], # España
    "maldita_ciencia": ["es", "from:"], # España
    "EFEVerifica": ["es", "from:"], # España
    "Chequeado": ["es", "from:"], # Argentina
    "Newtral": ["es", "from:"], # España
    "FullFact":  ["en", "from:"], # Inglés
    "ElSabuesoAP": ["es", "from:"], # Mexico
    "cotejoinfo": ["es", "from:"], # Venezuela
    "ECUADORCHEQUEA": ["es", "from:"], # Ecuador
    "lasillavacia": ["es", "from:"], # Colombia
    "AP": ["en", "from:"], # US
    "AfricaCheck": ["en", "from:"], # Africa
    "aosfatos": ["pt", "from:"], # Brasil
    "AAPNewswire": ["en", "from:"], # Australia
    "boomlive_in": ["en", "from:"], # India
    "correctiv_org": ["de", "from:"], # Alemania
    "Check_Your_Fact": ["en", "from:"], # USA
    "CheckCongo": ["fr", "from:"], # Congo
    "DemagogPL": ["pl", "from:"], # Polonia
    "dubawaNG": ["en", "from:"], # Nigeria
    "estadaoverifica": ["pt", "from:"], # Brasil
    "FactlyIndia": ["en", "from:"], # India
    "FactCrescendo": ["en", "from:"], # India
    "FactCheckNI": ["en", "from:"], # United Kingdom
    "ghana_fact": ["en", "from:"], # Ghana
    "Fatabyyano_com": ["ar", "from:"], # Jordania
    "FerretScot": ["en", "from:"], # United Kingdom (Scotland)
    "Observateurs": ["fr", "from:"], # Francia
    "lemondefr": ["fr", "from:"], # Francia
    "CheckNewsfr": ["fr", "from:"], # Australia
    "LogicallyAI": ["en", "from:"], # United Kingdom
    "MaharatNews": ["ar", "from:"], # Libano
    "Poynter": ["en", "from:"], # Internacional
    "mediawise": ["en", "from:"], # USA
    "NewsMobileIndia": ["en", "from:"], # India
    "NewsMeter_In": ["en", "from:"], # India
    "observadorpt": ["pt", "from:"], # Portugal
    "PesaCheck": ["en", "from:"], # Kenya
    "JornalPoligrafo": ["pt", "from:"], # Portugal
    "ABCFactCheck": ["en", "from:"], # Australia
    "rapplerdotcom": ["en", "from:"], # Filipinas
    "ReutersAgency": ["en", "from:"], # United States
    "ClimateFdbk": ["en", "from:"], # France
    "eye_digit": ["en", "from:"], # India
    "SouthAsiaCheck": ["en", "from:"], # Nepal
    "StopFakingNews": ["ru", "from:"], # Ucrania
    "IndiaToday": ["en", "from:"], # India
    "factchecknet": ["en", "from:"], # Internacional
    "thedispatch": ["en", "from:"], # USA
    "ThipMedia": ["en", "from:"], # India
    "TheQuint": ["en", "from:"], # India
    "GlennKesslerWP": ["en", "from:"], # chief writer of Washington Post's Fact Checker
    "thejournal_ie": ["en", "from:"], # Ireland
    "USATODAY": ["en", "from:"], # USA
    "verafiles": ["en", "from:"], # Filipinas
    "newsvishvas": ["en", "from:"], # India
    "dpa": ["de", "from:"], # Alemania
    "dogrulukpayicom": ["tr", "from:"], # Turquia
    "PagellaPolitica": ["it", "from:"], # Italia
    "teyitorg": ["tr", "from:"], # Turquia
    "NUnl": ["nl", "from:"], # Holanda
    "snopes": ["en", "from:"], # USA
    "franceinfo": ["fr", "from:"], # France
    
    
    # America newspapers
    "JustiaLatinAmer": ["es", "from:"], # Latino América
    "ReutersLatam": ["es", "from:"], # Latino América
    "UniNoticias": ["es", "from:"], # Latino América
    "14ymedio": ["es", "from:"], # Cuba
    "prensa_libre": ["es", "from:"], # Guatemala (Recommended by The Guardian)
    "ABCDigital": ["es", "from:"], # Paraguay (Recommended by The Guardian)
    "ObservadorUY": ["es", "from:"], # Urugay (Recommended by The Guardian) 
    "Milenio": ["es", "from:"], # México (Recommended by The Guardian)
    "ElMercurio_cl": ["es", "from:"], # Chile (Recommended by The Guardian)
    "elcomerciocom": ["es", "from:"], # Ecuador (Recommended by The Guardian)
    "ElMundoBolivia": ["es", "from:"], # Bolivia (Recommended by The Guardian)
    "laprensa": ["es", "from:"], # Nicaragua (Recommended by The Guardian)
    "elespectador": ["es", "from:"], # Colombia (Recommended by The Guardian)
    
    # America newspapers renowed
    "Pajaropolitico": ["es", "from:"], # from Poynter
    "elcomerciodigit": ["es", "from:"], # The Trust Project Perú
    "LANACION": ["es", "from:"], # The Trust Project Argetina
    "ElUniversal": ["es", "from:"], # The Trust Project Venezuela
    
    # US newspapers
    "nytimes": ["en", "from:"], # US
    "AmPress": ["en", "from:"], # US
    
    # Spain newspapers
    "el_pais": ["es", "from:"],
    "eldiarioes": ["es", "from:"],
    "elmundoes": ["es", "from:"],
    "EFEnoticias":  ["es", "from:"],
    "abc_es": ["es", "from:"],
    "telediario_tve": ["es", "from:"],
    "24h_tve": ["es", "from:"],
    
    # International newspaper
    "bbcmundo": ["es", "from:"], # Internacional
    
    # MEdical magazines from Spain
    "diariomedico": ["es", "from:"],
    "Consalud_es": ["es", "from:"],
    "redaccionmedica": ["es", "from:"],
    "VaccineSafetyN": ["en", "from:"]

}

# Feel free to modify the Twitter accounts showed above
# dic_user = {
#     # "US_FDA": ["en", "from:"]     
#     "el_pais": ["es", "from:"],
#     "EFEnoticias":  ["es", "from:"],
#     "abc_es": ["es", "from:"],
#     "telediario_tve": ["es", "from:"],
#     "24h_tve": ["es", "from:"],
#     "franceinfo": ["fr", "from:"]
#     }


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

def print_tweets_source_info(dic_user):
    print("""Twitter accounts used by default:""")
    print(sorted(list(dic_user.keys())))
    sys.exit()
    
if options.tweets_source_info:
    print_tweets_source_info(dic_user)    
    
    
if not all([options.api_key, options.api_secret_key,
            options.access_token, options.access_token_secret
            ]) or options.help:
    print_usage() 
    
if options.today: #  and not options.yesterday: 
    # Create date starting from 00:00h
    now_datetime = datetime.datetime.now()
    since_date = now_datetime.replace(hour=23, minute=59, second=59,
                                      microsecond=999999)
    
if options.day:
    since_date = datetime.datetime.now() - datetime.timedelta(options.day)
    since_date = since_date.replace(hour=23, minute=59, second=59, 
                                   microsecond=999999)
# Default number of tweets
if not options.count:
    options.count = 200
    


# CREDENTIALS for Twitter API   
api_key = options.api_key
api_secret_key = options.api_secret_key
access_token = options.access_token
access_token_secret = options.access_token_secret


# GitHub option
if options.git_token and options.git_repo:
    g = Github(options.git_token)
    repo = g.get_repo(options.git_repo)
    print("----------- Saving tweets on GitHub: {}-----------".format(repo)) 
    
    if options.git_autor:
        autor = options.git_autor
    else:
        autor = "Huertas97"

    if options.git_autor_email:
        email = options.git_autor_email
    else:
        email = "ahuertasg01@gmail.com"

else: 
    print("----------- Tweets will not be stored on GitHub -----------")    
    

# Local option
if options.save_local:
    print("----------- Saving tweets locally on: {} -----------".format(options.local_path)) 
else: 
    print("----------- Tweets will not be stored locally -----------")  


# Save in MongoDB
if all([options.mongo_user, options.mongo_pass, options.mongo_dbname,
                options.mongo_collection]):
    print("----------- Saving tweets on MongoDB. db: {}, collection: {} -----------".format(options.mongo_dbname,
                                                                                            options.mongo_collection)) 
else: 
    print("----------- Tweets will not be stored on MongoDB-----------")  

# STARTING Twitter API
twitter = OAuth1Session(api_key,
                        client_secret=api_secret_key,
                        resource_owner_key=access_token,
                        resource_owner_secret=access_token_secret)

## Access to the App per user 
# OAuth 1a (application-user). Rate limit: 180 requests in 15 min window
# auth = tweepy.OAuthHandler(api_key, api_secret_key)
# auth.set_access_token(access_token, access_token_secret)

## Access to the App directly (more amount of requests available)
# OAuth 2 (application-only). Rate limit: 450 requets in 15 min window
auth = tweepy.AppAuthHandler(api_key, api_secret_key)

# When we set wait_on_rate_limit to True, we will have our program wait
# automatically 15 minutes so that Twitter does not lock us out, whenever we
# exceed the rate limit and we automatically continue to get new data!
api = tweepy.API(auth, wait_on_rate_limit=True)




# today = datetime.date.today()
date = since_date.date()
print(date)




def json2dic(file_name, root):
    file_path = os.path.join(root, file_name)
    with open(file_path) as f:
        data = json.load(f)
    return data




for key, value in tqdm(dic_user.items(), desc="Progess"):
    user_name = key
    language = value[0]
    text_query = value[1]
    try:
        result_type = value[2]
    except:
        result_type = "recent"
    tweets_df = tweet_collect(count = options.count,
                              language = language,
                              text_query = text_query,
                              user_name = user_name,
                              result_type = result_type,
                              since_date=since_date
                              )
    
    
    
    # If a df is returned push it
    if isinstance(tweets_df, pd.DataFrame):
        
        
        # Save locally
        if options.save_local:
            # create folders and move json file to that folder by date
            local_folder = os.path.join(options.local_path, str(date))
            os.makedirs(local_folder, exist_ok=True)
            local_file_name = user_name+"-"+str(date)+".json"
        
            # Pandas df to json format
            tweets_df.to_json(os.path.join(local_folder, local_file_name))
        
        

        # Save on GitHub
        if options.git_token and options.git_repo:
            # create folders and move json file to that folder by date
            os.makedirs(os.path.join("./tweets", str(date)), exist_ok=True)
            git_file_name = user_name+"-"+str(date)+".txt"
            git_file_path = os.path.join("./tweets", str(date), git_file_name)
            
            # Extract tweets_id and save it as txt
            tweets_df["tweet_id"].to_csv(git_file_path, header=None, index=None, sep=' ', mode='w')

            # GitHub will only receive tweets ids (Twitter Privacy Conditions)
            # Extract the content to push
            file_content = open(git_file_path.replace("\\","/") , "r").read()
            push(path = git_file_path.replace("\\","/"), message = "Tweets from: " + str(date), content = file_content,
                 author = autor, author_mail = email)
            
        # Save on MongoDB
        if all([options.mongo_user, options.mongo_pass, options.mongo_dbname,
                options.mongo_collection]):
            mongo_file_name = user_name+"-"+str(date)+".json"

            mongo_user = options.mongo_user
            mongo_pass = options.mongo_pass
            mongo_dbname = options.mongo_dbname
            mongo_collection = options.mongo_collection
            client = MongoClient("mongodb+srv://" + mongo_user + ":" +
                             mongo_pass + "@fact-check-tweet-collec.oaort.mongodb.net/" + 
                             mongo_dbname + "?retryWrites=true&w=majority")
            db = client[mongo_dbname]  # ["fact-check-tweet-collection"]
            collection = db[mongo_collection]
            
            
            # Check and delete if file already exists in MongoDB collection 
            creation_date =  tweets_df.created_at.to_list()[0]
            collection.find_one_and_delete({ "screen_name.0": user_name, "created_at.0": str(creation_date) })
            # print(tweets_df.head())
        
            if mongo_file_name.split("-")[0] in checked_users: 
                json_file = tweets_df.to_json()
                mongo_file_content = json.loads(json_file)
                collection.insert_one(mongo_file_content)
            
        
        
        
    
