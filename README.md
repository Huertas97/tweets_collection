![GitHub language count](https://img.shields.io/github/languages/count/Huertas97/tweets_collection?style=plastic) ![GitHub watchers](https://img.shields.io/github/watchers/Huertas97/tweets_collection?style=social)


# Index
 
 * [Information](#information)
 * [General schema](#general-schema)
 * [Tweets hydratation and dehydratation](#tweets-hydratation-and-dehydratation)
 * [Usage and Examples](#usage-and-examples)


# **Information** 

Repository where tweets extracted from various Twitter accounts and hastags (total 200) are stored from October 1, 2020. The tweets extracted from the previous day are added daily. Although no content filter is applied to the extracted tweets (e.g. the term COVID-19 is not required to appear in the tweet), the hastags and accounts have been manually selected depending on whether their content fits the current COVID-19 health emergency situation. Feel free to add or change the Twitter accounts.  

The extracted tweets are organized by date (day) and by user or hastags. The extracted tweets can be locally saved as json format, uploaded to MongoDB as JSON files, or uploaded to GitHub as txt files only with the tweet ids (dehydrated). Accounts without tweets do not create any file. The information in the json files (hydrated) is:

 * account name
 * tweet id
 * full text (both tweet and retweet)
 * verification of the account
 * tweet date creation
 * fecha de creación del tweet
 * nº of times retweeted
 * favourites count
 * tweet location (if available)
 * account url 
 * tweet entities (url, hastags, etc)

# Tweets hydratation and dehydratation
Due to Twitter’s Developer terms and research ethics, most tweets we can acquire from Twitter’s Application Programming Interface (API) and third-party databases are dehydrated tweets. This is, instead of sharing tweet contents, geolocations, time, images, and other attached information to tweets, what researchers would initially share is a plain text file consisting of a list of unique tweet IDs. These IDs allow us to retrieve all tweet metadata, including the text, and they need to be “hydrated” to recover the metadata and to become meaningful research sources. The large size of tweets’ correlated data is another reason why datasets offer only dehydrated IDs. In this repository, a script for hydrating and dehydrating tweets is available. More information in [Usage](#usage), 

# General schema


[![](https://mermaid.ink/img/eyJjb2RlIjoiZ3JhcGggVEJcbkFbVHdpdHRlciBVc2VybmFtZV0gLS0-IEIoIFR3aXR0ZXIgQVBJIGZhOmZhLXR3aXR0ZXIgLilcbkIgLS0-IHwgVHdlZXRfd3JhcHBlcl92Mi5weXwgQ1tUd2VldHMgaW5mb3JtYXRpb24gZXh0cmFjdGVkXSBcbkMgLS0-IHxEZWh5ZHJhdGV8IEQoVFhUIGZpbGUgZmE6ZmEtZmlsZS10ZXh0IC4gKVxuRCAtLT58VXBsb2FkfCBFW0dpdEh1YiBmYTpmYS1naXRodWIgLl1cbkQgLS0-ICB8aHlkcmF0ZWRfdHdlZXRzLnB5fCBGXG5GIC0tPiB8dXBsb2FkX21vbmdvLnB5fCBHW01vbmdvREIgZmE6ZmEtZGF0YWJhc2UgLl1cblxuQyAtLT4gfFNhdmUgbG9jYWxseXwgRlsgSlNPTiBmaWxlIGZhOmZhLWZpbGUgLiAgXSBcbkMgLS0-IHxVcGxvYWR8IEdcblxuXG5cbiIsIm1lcm1haWQiOnsidGhlbWUiOiJuZXV0cmFsIn0sInVwZGF0ZUVkaXRvciI6ZmFsc2V9)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoiZ3JhcGggVEJcbkFbVHdpdHRlciBVc2VybmFtZV0gLS0-IEIoIFR3aXR0ZXIgQVBJIGZhOmZhLXR3aXR0ZXIgLilcbkIgLS0-IHwgVHdlZXRfd3JhcHBlcl92Mi5weXwgQ1tUd2VldHMgaW5mb3JtYXRpb24gZXh0cmFjdGVkXSBcbkMgLS0-IHxEZWh5ZHJhdGV8IEQoVFhUIGZpbGUgZmE6ZmEtZmlsZS10ZXh0IC4gKVxuRCAtLT58VXBsb2FkfCBFW0dpdEh1YiBmYTpmYS1naXRodWIgLl1cbkQgLS0-ICB8aHlkcmF0ZWRfdHdlZXRzLnB5fCBGXG5GIC0tPiB8dXBsb2FkX21vbmdvLnB5fCBHW01vbmdvREIgZmE6ZmEtZGF0YWJhc2UgLl1cblxuQyAtLT4gfFNhdmUgbG9jYWxseXwgRlsgSlNPTiBmaWxlIGZhOmZhLWZpbGUgLiAgXSBcbkMgLS0-IHxVcGxvYWR8IEdcblxuXG5cbiIsIm1lcm1haWQiOnsidGhlbWUiOiJuZXV0cmFsIn0sInVwZGF0ZUVkaXRvciI6ZmFsc2V9)

# Usage and Examples

First step is to clone the repository: 
`$ git clone https://github.com/Huertas97/tweets_collection.git`

Or download only the file Tweet_wrapper_v2.py if you want to extract only tweets. The accounts used for extracting the tweets can be modified in this code. 
Once downloaded, if you try to use the program it will most likely not work since a number of specific libraries are required. The program notifies which are these libraries. You can find these packages required in requirements.txt with the version used in this repository. 

Likewise, the program's help can be accessed with the command:
`$ python Tweet_wrapper_v2.py --help`

Output:
```
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
     
     Furthermore, you should have a GitHub account and a Twitter Developer API
     credentials. 

Example. 

Collect up to 100 tweets from today, save them locally and on GitHub:
    $ python Tweet_wrapper_v2.py -t -c 100 \
        --save_local --local_path "../local_tweets" \
        --git_token XXX --git_repo Huertas97/tweets_collection \
        --api_key XXX --api_secret_key XXX --access_token XXX --access_token_secret XXX
        
Collect up to 200 tweets from yesterday, save them locally (not GitHub): 
    $ python Tweet_wrapper_v2.py -d 1 -c 200 \
        --save_local --local_path "../local_tweets" \
        --api_key XXX --api_secret_key XXX --access_token XXX --access_token_secret  XXX

Collect up to 40 tweets from 4 days ago, save them locally and on MongoDB (not GitHub): 
    $ python Tweet_wrapper_v2.py -d 4 -c 40 \
        --save_local --local_path "../local_tweets" \
        --mongo_user Huertas97 --mongo_pass XXX  \
        --mongo_dbname fact-check-tweet-collection \
        --mongo_collection tweets
        --api_key XXX --api_secret_key XXX --access_token XXX --access_token_secret XXX
```
    
Also, you can consult the Twitter accounts used by:

`$ python Tweet_wrapper_v2.py --tweets_source_info `

```
Twitter accounts used by default:
['#FactCHAT', '#FakePCR', '#PCRFraude', '#VacunaRusa', '#VirusChino', '1333Despierta', '14ymedio', '20m', '24h_tve', 'AAPNewswire', 'ABCDigital', 'ABCFactCheck', 'AEMPSGOB', 'ANTIMASCARILLA', 'AP', 'ActualidadRT', 'AfricaCheck', 'Africamar', 'AlbaGar74381296', 'AmPress', 'Angelisimo2', 'AquAhora1', 'AtraviesaLoDesc', 'Autnomacabread1', 'BabylonDab', 'CDCespanol', 'CDCgov', 'CancerIntegral', 'CarmCerb21', 'CellPressNews', 'CheckCongo', 'CheckNewsfr', 'Check_Your_Fact', 'Chequeado', 'ChiguireBipolar', 'ClimateFdbk', 'Consalud_es', 'DathosBD', 'DemagogPL', 'DiegoMo53772865', 'ECUADORCHEQUEA', 'EFEVerifica', 'EFEnoticias', 'ELMINIMALISTA1', 'ElMercurio_cl', 'ElMundoBolivia', 'ElSabuesoAP', 'ElTrompetista78', 'ElUniversal', 'FDA_Drug_Info', 'FDAenEspanol', 'FDArecalls', 'FactCheckNI', 'FactCrescendo', 'FactlyIndia', 'Fatabyyano_com', 'FerretScot', 'FoxMuld88326271', 'FrayJosepho', 'FullFact', 'GlennKesslerWP', 'HayNoticia', 'HerbolarioLola', 'HomeopatiaY', 'HopkinsMedicine', 'IndiaToday', 'IsTortugo', 'JL_MDesconocido', 'JordiFlynn', 'JornalPoligrafo', 'JosPastr', 'JustiaLatinAmer', 'LANACION', 'LRsecreta', 'LaRetuerka', 'LaVozIberica', 'LaVozdelBecario', 'LogicallyAI', 'MaharatNews', 'MayoClinic', 'MediterraneoDGT', 'MiHerbolario', 'Milenio', 'Musicolorista', 'NEJM', 'NIH', 'NUnl', 'NatureComms', 'NaturopatasCol', 'NewsMeter_In', 'NewsMobileIndia', 'Newtral', 'NiusDiario', 'NoHayPandemia__', 'No__Plandemia', 'NoalaVacuna', 'ObservadorUY', 'Observateurs', 'POTUS_Trump_ESP', 'PacienteL', 'PagellaPolitica', 'Pajaropolitico', 'PericoAFuego', 'PesaCheck', 'Plandemia', 'PorunChileDigno', 'Poynter', 'ProgreAzote', 'ReutersAgency', 'ReutersLatam', 'SaludPublicaEs', 'SouthAsiaCheck', 'StopFakingNews', 'TheBabylonBee', 'TheOnion', 'TheQuint', 'The_Cling_On', 'ThipMedia', 'TrendsMolecMed', 'USATODAY', 'US_FDA', 'UniNoticias', 'VaccineSafetyN', 'VaccineXchange', 'WHO', 'YoNoMeVacuno', '_nWorder', 'abc_es', 'actualidadpanam', 'andaluciadatos', 'aosfatos', 'bbcmundo', 'boomlive_in', 'coronatimo', 'correctiv_org', 'cotejoinfo', 'covid1984', 'diariomedico', 'doctor_papaya', 'dogrulukpayicom', 'dpa', 'dubawaNG', 'el_pais', 'elcomerciocom', 'elcomerciodigit', 'eldiarioes', 'elentirvigo', 'elespectador', 'eljueves', 'elmundoes', 'elmundotoday', 'elphabaz', 'embojournal', 'estadaoverifica', 'eye_digit', 'factchecknet', 'franceinfo', 'ghana_fact', 'gonzo_blogger', 'guardiacivil', 'hermanntertsch', 'informate_infor', 'lamjort', 'laprensa', 'lasillavacia', 'ldpsincomplejos', 'lemondefr', 'maldita_ciencia', 'malditobulo', 'mediawise', 'mitokondriac', 'newsvishvas', 'nytimes', 'observadorpt', 'okdiario', 'opsoms', 'panguerrera1', 'papayaykware', 'patrilaselma', 'periodistadigit', 'policia', 'prensa_libre', 'rapplerdotcom', 'redaccionmedica', 'researchnews', 'revisbarcelona', 'sanidadgob', 'snopes', 'tecn_preocupado', 'telediario_tve', 'teyitorg', 'the_raven77', 'thecliniccl', 'thedispatch', 'thejournal_ie', 'tiramillas', 'trustdall271', 'velardedaoiz2', 'verafiles', 'yonomeconfino']
```


For hydrating tweets available as txt files in the repository use `hydrate_tweets.py`:



```
$ python hydrate_tweets.py --help

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
    --access_token_secret        ACCESS TOKEN SECRET
    --tweets_path                Path where the tweets to hydrate are located
    --help                       Help documentation

Example.
    $ python hydrate_tweets.py --api_key XXX --api_secret_key XXX --access_token XXX \
        --access_token_secret XXX --tweets_path tweets/
```

For dehydrating tweets JSON files downloaded locally use `dehydrate_tweets.py`:

```
$ python dehydrate_tweets.py --help

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
```

For uploading to MongoDB hydrated JSON files use `upload_mongo.py`:

```
python upload_mongo.py --help

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

```


